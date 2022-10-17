from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Use Selenium and BeautifulSoup to web scrape from zolo.ca

# Open zolo.ca on Firefox
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.get("https://www.zolo.ca/")

location = "v5g"  # Make this user inputted using node.js
house_sqft = 1000 # Make this user inputted
driver.find_element(By.ID, "sarea").clear()
element = driver.find_element(By.ID, "sarea")
element.send_keys(location)
element.send_keys(Keys.RETURN)  # Enters the desired location in the search bar

time.sleep(2)

# Use webscraper on website
url = driver.current_url  # Gets the URL of the page from the desired location
request_page = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_page).read()
# webpage.close()

html_soup = BeautifulSoup(webpage, 'html.parser')

house_items = html_soup.find_all('div', class_="card-listing--details")

filename = 'local_house_info.csv'
f = open(filename, 'w')

headers = 'Price,Size\n'

f.write(headers)

for house in house_items:
    price = 'Null'
    size = 'Null'
    if house.find('span', itemprop="price") != None:
        price = house.find('span', itemprop="price").text
        price = price.replace(',', '')

        extra_info = house.find_all('li', class_="xs-inline")
        for info in extra_info:
            if (info.text).endswith('sqft'):
                size = info.text

    f.write(price + ',' + size + '\n')

f.close()
