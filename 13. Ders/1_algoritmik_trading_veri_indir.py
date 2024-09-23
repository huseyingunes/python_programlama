import json
from binance.client import Client
from datetime import datetime
from binance.helpers import date_to_milliseconds

symbol = "ADAUSDT"
start = "1 Jan, 2020"
end = "30 Dec, 2023"
interval = Client.KLINE_INTERVAL_1DAY

client = Client()

klines = client.get_historical_klines(symbol, interval, start, end)

csv_file = open("veri/BTCUSDT1yilGunluk.csv", "w")

csv_file.write("otime,open,high,low,close,volume\n")
for line in klines:
    csv_file.write(str(datetime.fromtimestamp(int(line[0]/1000)))+","+str(line[1])+","+str(line[2])+","+str(line[3])+","+str(line[4])+","+str(line[5])+"\n")

