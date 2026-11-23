import plotly.graph_objects as go
import streamlit as st

def render_price_chart(df, ticker):
    st.subheader(f"{ticker} price history")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"],
        name="Price"
    ))
    for column, label in [("SMA_20", "SMA 20"), ("SMA_50", "SMA 50"), ("SMA_200", "SMA 200")]:
        if column in df:
            fig.add_trace(go.Scatter(x=df.index, y=df[column], name=label, mode="lines"))
    fig.update_layout(template="plotly_dark", height=570, xaxis_rangeslider_visible=False,
                      legend_orientation="h", margin=dict(t=25,b=20,l=10,r=10))
    st.plotly_chart(fig, use_container_width=True)
    volume = go.Figure(go.Bar(x=df.index, y=df["Volume"], name="Volume"))
    volume.update_layout(template="plotly_dark", height=220, margin=dict(t=10,b=10,l=10,r=10))
    st.plotly_chart(volume, use_container_width=True)
