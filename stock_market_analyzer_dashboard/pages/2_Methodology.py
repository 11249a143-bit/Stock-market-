import streamlit as st
st.set_page_config(page_title="Methodology · Stock Analyzer", page_icon="🧮", layout="wide")
st.title("Calculation methodology")
st.markdown("""
- Prices are downloaded with `auto_adjust=True`; OHLC values are adjusted where supported by the provider.
- Daily return = current close / previous close - 1.
- Period return = last close / first close - 1.
- Annualized volatility = standard deviation of periodic returns × square root of 252 for daily observations.
- Maximum drawdown = portfolio wealth / running peak - 1, taking the minimum value.
- SMA uses rolling arithmetic means; RSI, MACD and Bollinger Bands are calculated with the `ta` package.
""")
st.caption("Annualization assumes daily trading observations. For weekly/monthly intervals, the current simple risk summary still uses a daily-frequency assumption and should be interpreted cautiously.")
