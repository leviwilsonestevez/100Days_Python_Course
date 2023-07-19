from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, 'html.parser')

URL = "https://tradingeconomics.com/country-list/gdp-annual-growth-rate"
dr = webdriver.Chrome()
dr.get(URL)
bs = BeautifulSoup(dr.page_source, "html.parser")

th_headers = bs.select("tr th")
for header in th_headers:
    pprint(header.text)

pprint("-------------------------------------------------")
td_data = bs.select("tr td")
for data in td_data:
    pprint(data.text)

pprint("-------------------------------------------------")
for row in bs.table.find_all('tr')[1:]:
    print(row.td.text)
