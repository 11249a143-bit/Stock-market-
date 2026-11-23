import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands

def add_indicators(history):
    df = history.copy()
    close = df["Close"]
    df["SMA_20"] = close.rolling(20, min_periods=20).mean()
    df["SMA_50"] = close.rolling(50, min_periods=50).mean()
    df["SMA_200"] = close.rolling(200, min_periods=200).mean()
    df["EMA_20"] = close.ewm(span=20, adjust=False).mean()
    df["RSI_14"] = RSIIndicator(close=close, window=14).rsi()
    macd = MACD(close=close)
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    df["MACD_Diff"] = macd.macd_diff()
    bands = BollingerBands(close=close, window=20, window_dev=2)
    df["BB_Upper"] = bands.bollinger_hband()
    df["BB_Middle"] = bands.bollinger_mavg()
    df["BB_Lower"] = bands.bollinger_lband()
    df["Daily_Return"] = close.pct_change()
    df["Cumulative_Return"] = (1 + df["Daily_Return"].fillna(0)).cumprod() - 1
    return df
