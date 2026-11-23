import streamlit as st
st.set_page_config(page_title="About · Stock Analyzer", page_icon="ℹ️", layout="wide")
st.title("About this dashboard")
st.write(
    "This educational dashboard downloads historical market prices using yfinance "
    "and calculates common technical, performance and risk indicators."
)
st.subheader("Indicators included")
st.markdown("""
- **SMA / EMA:** moving averages of historical closing prices.
- **RSI:** momentum oscillator, commonly calculated over 14 periods.
- **MACD:** moving-average convergence/divergence and signal line.
- **Bollinger Bands:** rolling mean with upper/lower volatility bands.
- **Volatility:** annualized standard deviation of periodic returns.
- **Maximum drawdown:** largest peak-to-trough decline in the selected sample.
""")
st.warning("This dashboard is for education and research. It does not provide personalized investment advice or guarantee future results.")
