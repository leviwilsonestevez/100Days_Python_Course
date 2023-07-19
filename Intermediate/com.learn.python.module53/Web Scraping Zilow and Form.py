

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,"
    "-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C"
    "%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37"
    ".69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C"
    "%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue"
    "%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value"
    "%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A"
    "%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp"
    "%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C"
    "%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")
all_link_elements = soup.find_all('a', class_="property-card-link")

all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_price_elements = soup.select('span', class_='srp__sc-16e8gqd-1 jLQjry')

all_address_elements = soup.select("address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_prices = []
for span in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        price = ""
        # Price with only one listing
        if "$" in span.get_text():
            price = span.get_text()
            all_prices.append(price)
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        if "$" in span.get_text():
            price = span.get_text()
            all_prices.append(price)

# Create Spreadsheet using Google Form
# Substitute your own path here 👇
chrome_driver_path = "C:/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
LINK_FORM_SF_RENTING_FORM = "https://docs.google.com/forms/d/e" \
                            "/1FAIpQLSfEnDsG8yg1hv5YYri51rH_9vylBMOZSXycbD59O4XDajBVYA/viewform?usp=sf_link "

RECORTED_FORM_LINK = "https://forms.gle/S3SMTqDkcBB65JDy7"
for n in range(len(all_links)):
    # Substitute your own Google Form URL here 👇
    driver.get(RECORTED_FORM_LINK)

    time.sleep(2)
    address = driver.find_element(By.XPATH, value=
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, value=
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, value=
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
