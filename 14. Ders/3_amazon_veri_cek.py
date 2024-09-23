"""
amazon.com'dan müşteri yorumlarını selenium ile çekmek için
gerekli kodu yazınız
"""
from selenium import webdriver
import time
import os
import json

def get_amazon_reviews(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    reviews = driver.find_elements_by_css_selector(".review-text-content")
    reviews = [review.text for review in reviews]
    driver.close()
    return reviews

def main():
    url = "https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/product-reviews/B07P6Y7954/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    reviews = get_amazon_reviews(url)
    with open("amazon_reviews.txt", "w") as file:
        for review in reviews:
            file.write(review + "\n")

if __name__ == "__main__":
    main()
    