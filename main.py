from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.chrome.options import Options

currencies = {}

# GOING PAGE
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get("https://coinmarketcap.com")

#TAKING SOURCE
coinmarketcap_source = browser.page_source
soup = BeautifulSoup(coinmarketcap_source, 'html.parser')
table = soup.find_all("tr", {"class":"cmc-table-row"})

for table in table:
    name = table.find("td", {"class":"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).text
    price = table.find("td", {"class":"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).text
    currencies[name] = price

# BROWSER CLOSE
browser.close()

# GETTING CHOICE
choice = input("Hangi kripto paranın fiyatını öğrenmek istiyorsunuz: ")

# SHOWING PRICE
if choice in currencies:
    print("{currency_name}:".format(currency_name = choice), currencies[choice])

else:
    print("Bu isimde bir kripto para bulunmamaktadır.")