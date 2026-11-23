import streamlit as st

def render_metrics(df, performance, risk):
    latest = float(df["Close"].iloc[-1])
    previous = float(df["Close"].iloc[-2]) if len(df) > 1 else latest
    daily_change = latest / previous - 1 if previous else 0
    columns = st.columns(5)
    columns[0].metric("Latest close", f"{latest:,.2f}", f"{daily_change:+.2%}")
    columns[1].metric("Period return", f"{performance['period_return']:+.2%}")
    columns[2].metric("Annualized volatility", f"{risk['volatility']:.2%}")
    columns[3].metric("Maximum drawdown", f"{risk['max_drawdown']:.2%}")
    columns[4].metric("Best daily return", f"{performance['best_day']:+.2%}")
