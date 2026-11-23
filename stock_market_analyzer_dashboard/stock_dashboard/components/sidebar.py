import streamlit as st

def render_sidebar(default_ticker, default_period, period_options):
    with st.sidebar:
        st.header("Market settings")
        ticker = st.text_input("Ticker symbol", value=default_ticker, help="Examples: AAPL, MSFT, RELIANCE.NS, TCS.NS").strip()
        labels = list(period_options.keys())
        default_label = next((k for k, v in period_options.items() if v == default_period), "1 year")
        period_label = st.selectbox("Historical period", labels, index=labels.index(default_label))
        interval = st.selectbox("Interval", ["Daily", "Weekly", "Monthly"])
        interval_value = {"Daily": "1d", "Weekly": "1wk", "Monthly": "1mo"}[interval]
        submitted = st.button("Analyze stock", type="primary", use_container_width=True)
        st.divider()
        st.caption("Data source: Yahoo Finance via yfinance. Data may be delayed or unavailable.")
    return ticker, period_options[period_label], interval_value, submitted
