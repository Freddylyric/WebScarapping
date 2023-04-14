# import requests
# from bs4 import BeautifulSoup
# import csv

# r = requests.get('https://www.futurepedia.io/')
# soup = BeautifulSoup(r.text, 'html.parser')

# f = csv.writer(open('dataprocessing.csv', 'w'))
# f.writerow(['title', 'content'])
# f.writerow([soup.title.text, soup.find_all('p')[0].text])
