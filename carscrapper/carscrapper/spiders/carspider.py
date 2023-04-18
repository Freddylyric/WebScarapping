import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
import json
import pymongo
from pymongo import MongoClient
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://freddykk20:{password}@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client["carDatabase"]
collection = database["cars"]


class CarRentalsSpider(scrapy.Spider):
    name = "car_rentals"
    start_urls = [
        'https://myhire.co.ke/car-rentals/?taxonomy%5Bst_category_cars%5D=46']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)

        raw_image_urls = sel.xpath(
            '//*[@id="modern-search-result"]/div[2]/div[1]/div/div[1]/div/a[2]/img/@src').getall()
        # convert relative url to proper url
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        # Extracting car name, price, image, and url
        car_listings = sel.css('div.item-service')

        for car in car_listings:
            name = car.css(
                'h4.service-title a::text').get().replace('CAR HIRE – ', '')
            price = car.css(
                'span.price').get().replace('<span class=\"price\">\n ', '').replace('</span>', '').strip()
            url = car.css('h4.service-title a').attrib['href']

            # Saving data as a dictionary
            car_data = {
                'name': name,
                'price': price,
                'image_urls': clean_image_urls,
                'url': url,
            }

            # Saving data as a JSON file
            with open('car_rentals_data.json', 'a') as f:
                f.write(json.dumps(car_data) + '\n')


        # Load the data from the JSON file
        with open('car_rentals_data.json') as f:
            data = [json.loads(line) for line in f]

        # Insert the data into MongoDB
        collection.insert_many(data)


        next_page = response.css('a.next.page-numbers::attr(href)').get()
        

        if next_page is not None:

            yield response.follow(next_page, callback=self.parse, dont_filter=True)

    def closed(self, reason):
        self.driver.quit()
