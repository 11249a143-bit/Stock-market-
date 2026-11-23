import streamlit as st

def render_empty_state():
    st.info("Enter a valid ticker symbol and select Analyze stock to load market data.")
    st.caption("Examples: AAPL (US), MSFT (US), RELIANCE.NS (India), TCS.NS (India).")
