"""
finnhub tan son 1 yılın 1 saatlik BTCUSDT verilerini çek
Bunların mum grafiğini matplotlib ile çizdir
MACD grafiğini ekle
"""

# ... existing code ...

import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

# Finnhub API Ayarları
API_KEY = "BURAYA_FINNHUB_API_KEY_GELECEK"  # Finnhub'dan alacağınız API anahtarını buraya yazın
SYMBOL = "BINANCE:BTCUSDT"
RESOLUTION = "60"  # 1 saatlik veriler (60 dakika)

def get_crypto_data():
    # Zaman hesaplaması: Şu anki zaman ve 1 yıl öncesi (Unix Timestamp)
    to_timestamp = int(time.time())
    from_timestamp = to_timestamp - (365 * 24 * 60 * 60)

    url = "https://finnhub.io/api/v1/crypto/candle"
    params = {
        "symbol": SYMBOL,
        "resolution": RESOLUTION,
        "from": from_timestamp,
        "to": to_timestamp,
        "token": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("s") == "ok":
        df = pd.DataFrame({
            "t": pd.to_datetime(data["t"], unit="s"),
            "o": data["o"],
            "h": data["h"],
            "l": data["l"],
            "c": data["c"],
            "v": data["v"]
        })
        return df
    else:
        print("Veri çekilemedi:", data)
        return None

def calculate_macd(df):
    # 12 ve 26 periyotluk Üstel Hareketli Ortalama (EMA)
    ema12 = df["c"].ewm(span=12, adjust=False).mean()
    ema26 = df["c"].ewm(span=26, adjust=False).mean()

    # MACD Hattı
    df["macd"] = ema12 - ema26
    # Sinyal Hattı (9 periyotluk EMA)
    df["signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    # Histogram
    df["hist"] = df["macd"] - df["signal"]
    return df

def plot_charts(df):
    # 2 satırlı bir grafik alanı oluştur (Üstte Mum, Altta MACD)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

    # --- Mum Grafiği Çizimi (Manuel) ---
    up = df[df.c >= df.o]
    down = df[df.c < df.o]

    width = 0.03  # Mum genişliği (yaklaşık 1 saatlik veri için görsel genişlik)

    # Yükselen Mumlar (Yeşil)
    ax1.vlines(up.t, up.l, up.h, color='green', linewidth=1)
    ax1.bar(up.t, up.c - up.o, bottom=up.o, width=width, color='green')

    # Düşen Mumlar (Kırmızı)
    ax1.vlines(down.t, down.l, down.h, color='red', linewidth=1)
    ax1.bar(down.t, down.o - down.c, bottom=down.c, width=width, color='red')

    ax1.set_title(f"{SYMBOL} - Son 1 Yıl (1 Saatlik)")
    ax1.set_ylabel("Fiyat")
    ax1.grid(True, alpha=0.3)

    # --- MACD Grafiği Çizimi ---
    ax2.plot(df.t, df["macd"], label="MACD", color="blue", linewidth=1.5)
    ax2.plot(df.t, df["signal"], label="Signal", color="orange", linewidth=1.5)

    # Histogram Renklendirme
    colors = ['green' if x >= 0 else 'red' for x in df["hist"]]
    ax2.bar(df.t, df["hist"], color=colors, width=width, alpha=0.5)

    ax2.set_title("MACD")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Veriler Finnhub'dan çekiliyor...")
    df = get_crypto_data()

    if df is not None:
        print("MACD hesaplanıyor...")
        df = calculate_macd(df)
        print("Grafik çiziliyor...")
        plot_charts(df)