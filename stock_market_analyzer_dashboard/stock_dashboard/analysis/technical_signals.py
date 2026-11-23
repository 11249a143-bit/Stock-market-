def indicator_snapshot(df):
    if df.empty:
        return {}
    row = df.iloc[-1]
    return {
        "close": row.get("Close"),
        "rsi": row.get("RSI_14"),
        "macd": row.get("MACD"),
        "macd_signal": row.get("MACD_Signal"),
        "sma_20": row.get("SMA_20"),
        "sma_50": row.get("SMA_50"),
        "sma_200": row.get("SMA_200"),
    }
