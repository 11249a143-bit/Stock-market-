def build_market_commentary(df):
    if df.empty:
        return {"overview": "No data available.", "trend": "Unavailable",
                "momentum": "Unavailable", "volatility": "Unavailable"}
    last = df.iloc[-1]
    close = float(last["Close"])
    sma50 = last.get("SMA_50")
    sma200 = last.get("SMA_200")
    rsi = last.get("RSI_14")
    bb_upper = last.get("BB_Upper")
    bb_lower = last.get("BB_Lower")

    if sma50 == sma50 and sma200 == sma200:
        trend = "Above long-term average" if close > sma200 else "Below long-term average"
    elif sma50 == sma50:
        trend = "Above 50-period average" if close > sma50 else "Below 50-period average"
    else:
        trend = "Insufficient history"

    if rsi == rsi:
        momentum = "Higher RSI range" if rsi >= 70 else "Lower RSI range" if rsi <= 30 else "Middle RSI range"
    else:
        momentum = "Insufficient history"

    if bb_upper == bb_upper and bb_lower == bb_lower and close:
        position = (close - bb_lower) / (bb_upper - bb_lower) if bb_upper != bb_lower else 0.5
        volatility = "Near upper band" if position > .8 else "Near lower band" if position < .2 else "Within bands"
    else:
        volatility = "Insufficient history"

    overview = (
        f"The latest close is {close:.2f}. The price is {trend.lower()}; "
        f"the RSI-based momentum classification is {momentum.lower()}, and the "
        f"Bollinger Band position is {volatility.lower()}. These are historical "
        "descriptions, not forecasts or personalized trading recommendations."
    )
    return {"overview": overview, "trend": trend, "momentum": momentum, "volatility": volatility}
