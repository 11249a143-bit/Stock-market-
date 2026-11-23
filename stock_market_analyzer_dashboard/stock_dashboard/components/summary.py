import streamlit as st

def render_summary(ticker, info, df):
    company = info.get("longName") or info.get("shortName") or ticker
    st.subheader(f"{company} ({ticker})")
    details = [info.get("sector"), info.get("industry"), info.get("currency")]
    st.caption(" · ".join(str(x) for x in details if x) or "Company metadata not available")
    if not df.empty:
        st.caption(f"Showing {len(df):,} observations · {df.index.min().date()} to {df.index.max().date()}")
