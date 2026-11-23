import plotly.graph_objects as go
import streamlit as st

def render_indicator_charts(df):
    st.subheader("Bollinger Bands")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["BB_Upper"], name="Upper band", line=dict(dash="dot")))
    fig.add_trace(go.Scatter(x=df.index, y=df["BB_Lower"], name="Lower band",
                             fill="tonexty", fillcolor="rgba(100,149,237,.12)"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Close"))
    fig.update_layout(template="plotly_dark", height=380, margin=dict(t=15,b=10,l=10,r=10))
    st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("Relative Strength Index (RSI)")
        rsi = go.Figure()
        rsi.add_trace(go.Scatter(x=df.index, y=df["RSI_14"], name="RSI 14"))
        rsi.add_hline(y=70, line_dash="dash")
        rsi.add_hline(y=30, line_dash="dash")
        rsi.update_layout(template="plotly_dark", height=300, yaxis_range=[0,100])
        st.plotly_chart(rsi, use_container_width=True)
    with right:
        st.subheader("MACD")
        macd = go.Figure()
        macd.add_trace(go.Scatter(x=df.index, y=df["MACD"], name="MACD"))
        macd.add_trace(go.Scatter(x=df.index, y=df["MACD_Signal"], name="Signal"))
        macd.add_trace(go.Bar(x=df.index, y=df["MACD_Diff"], name="Histogram"))
        macd.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(macd, use_container_width=True)
