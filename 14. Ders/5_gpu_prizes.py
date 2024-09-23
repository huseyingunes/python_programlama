"""
Farklı amazon sitelerinden tüm ekran kartlarının fiyatlarını çekip
bunları bir dosyaya yazan program yazınız.
"""
from selenium import webdriver
import time
import os
import json

def get_amazon_prices(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    prices = driver.find_elements_by_css_selector(".a-price-whole")
    prices = [price.text for price in prices]
    driver.close()
    return prices

def main():
    url = "https://www.amazon.com/s?k=graphics+card&ref=nb_sb_noss_2"
    prices = get_amazon_prices(url)
    with open("amazon_prices.txt", "w") as file:
        for price in prices:
            file.write(price + "\n")

if __name__ == "__main__":
    main()
