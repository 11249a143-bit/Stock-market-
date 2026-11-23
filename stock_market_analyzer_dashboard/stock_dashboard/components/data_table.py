import streamlit as st
from stock_dashboard.services.export_service import dataframe_csv_bytes

def render_data_table(df, ticker):
    st.subheader("Historical market data")
    st.dataframe(df.sort_index(ascending=False), use_container_width=True)
    st.download_button(
        "Download historical data (CSV)",
        dataframe_csv_bytes(df),
        file_name=f"{ticker}_historical_data.csv",
        mime="text/csv",
    )
