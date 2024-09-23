import json
from binance.client import Client
from datetime import datetime
from binance.helpers import date_to_milliseconds
from csv import reader
import csv
import pandas as pd
import numpy as np
import pandas_ta as ta

para = 100
bin_onceki_gun_verisi = None
alim_fiyati = None
alindi = False

veri = pd.read_csv("veri/BTCUSDT1yilGunluk.csv")
veri.ta.sma(length=30, append=True)
for kayit in veri.itertuples():
    if kayit[0] <= 1:
        bin_onceki_gun_verisi = kayit
    if kayit[0] > 11:
        if alindi:
            if kayit[5] < kayit[7]:
                alindi = False
                para = (kayit[5] * para) / alim_fiyati
                print(para)
        if bin_onceki_gun_verisi[5] < bin_onceki_gun_verisi[7] and kayit[5]>kayit[7]:
            alim_fiyati = kayit[5]
            alindi = True

        bin_onceki_gun_verisi = kayit
print("Sonuc :", para)

