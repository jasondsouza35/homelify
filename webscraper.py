from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import Keys

# Use Selenium and BeautifulSoup to web scrape from Realtor.ca

# Open realtor.ca
driver = webdriver.Chrome()
driver.get("https://www.realtor.ca/")

location = "l9t" #User inputed 
element = driver.find_element_by_id("homeSearchTxt")
element.send_keys(location, Keys.RETURN) # Types the desired location into the search bar and clicks the return key

url_to_scrape = driver.getCurrentUrl() # Gets the URL of the page from the desired location

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