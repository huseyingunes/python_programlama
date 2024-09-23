import mplfinance as fplt
import pandas_ta as ta
import yfinance as yf
data = yf.download("BTC-USD", period="3mo")

data.ta.sma(length=10, append=True)
print(data)
#print(data["Close"].max())
fplt.plot(
            data,
            type='candle',
            title='BTC USDT Aralık',
            ylabel='Fiyat ($)',
            mav=(10)
        )
