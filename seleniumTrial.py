# # from selenium import webdriver

# # path = r'C:/Users/Admin/Downloads/chromedriver_win32.zip/chromedriver'
# # browser = webdriver.Chrome(executable_path=path)

# # browser.get('https://www.futurepedia.io/')

# # browser.find_element_by_xpath('/html/body').click()









# import scrapy
# from scrapy.selector import Selector
# from selenium import webdriver
# from scrapy_selenium import SeleniumRequest
# import json
# import pymongo
# from pymongo import MongoClient


# cluster = "mongodb+srv://freddykk20:NBXkwlueiqfgfp2F@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(cluster)
# database = client["carDatabase"]
# collection = database["cars"]


# class CarRentalsSpider(scrapy.Spider):
#     name = "car_rentals"
#     start_urls = [
#         'https://myhire.co.ke/car-rentals/?taxonomy%5Bst_category_cars%5D=46']

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def start_requests(self):
#         for url in self.start_urls:
#             yield SeleniumRequest(url=url, callback=self.parse, dont_filter=True)

#     def parse(self, response):
#         self.driver.get(response.url)
#         sel = Selector(text=self.driver.page_source)

#         raw_image_urls = sel.xpath(
#         '//*[@id="modern-search-result"]/div[2]/div[1]/div/div[1]/div/a[2]/img/@src').getall()
#         # convert relative url to proper url
#         clean_image_urls = []
#         for img_url in raw_image_urls:
#             clean_image_urls.append(response.urljoin(img_url))

#         # Extracting car name, price, image, and url
#         car_listings = sel.css('div.item-service')

#         # create an empty list to hold the data dictionaries
#         data = []

#         for car in car_listings:
#             name = car.css(
#             'h4.service-title a::text').get().replace('CAR HIRE – ', '')
#             price = car.css(
#             'span.price').get().replace('<span class=\"price\">\n ', '').replace('</span>', '').strip()
#             url = car.css('h4.service-title a').attrib['href']

#             # Saving data as a dictionary
#             car_data = {
#             'name': name,
#             'price': price,
#             'image_urls': clean_image_urls,
#             'url': url,
#             }

#             # append the data dictionary to the list
#             data.append(car_data)

#         # Insert the data into MongoDB
#         if len(data) > 0:
#             collection.insert_many(data)

#         next_page = response.css('a.next.page-numbers::attr(href)').get()

#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse, dont_filter=True)


# # cluster = "mongodb+srv://freddykk20:NBXkwlueiqfgfp2F@cluster0.zjvwmxw.mongodb.net/?retryWrites=true&w=majority"
# # client = MongoClient(cluster)

# # print(client.list_database_names())

# # db = client.carDatabase

# # print(db.list_collection_names())
