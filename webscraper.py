from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.realtor.ca/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

house_items = html_soup.find_all('div', class_="")

filename = 'local_house_info.csv'
f = open(filename, 'w')

headers = 'Size, Price \n'

f.write(headers)

for house in house_items:
    size = house.find('div', class_="")
    price = house.find('div', class_="")

    f.write(title + ',' + price)

f.close()