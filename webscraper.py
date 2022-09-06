from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Use Selenium and BeautifulSoup to web scrape from Realtor.ca

# Open realtor.ca
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
driver.get("https://www.realtor.ca/")

location = "l9t" # User inputed 
#element = driver.find_element_by_id("homeSearchTxt")
element = driver.find_element("homeSearchTxt")
element.send_keys(location) # Types the desired location into the search bar
element.send_keys(Keys.ENTER)

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
    location = house.find('div', class_="smallListingCardAddress")
    price = house.find('div', class_="smallListingCardPrice")

    f.write(location + ',' + price)

f.close()