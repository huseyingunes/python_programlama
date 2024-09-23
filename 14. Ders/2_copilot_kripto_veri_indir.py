"""
Binance tan son 1 yılın BTCUSDt verisini çekip,
bu veriyi bir dosyaya yazan program yazınız.
"""
import requests
import json
import time
import datetime
import os

def get_btc_data():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def write_data(data):
    with open("btc_data.txt", "w") as file:
        for row in data:
            file.write(str(row) + "\n")

def main():
    data = get_btc_data()
    write_data(data)

if __name__ == "__main__":
    main()



