import streamlit as st
from dotenv import load_dotenv

from stock_dashboard.config import APP_TITLE, DEFAULT_TICKER, DEFAULT_PERIOD, PERIOD_OPTIONS
from stock_dashboard.services.market_data_service import MarketDataService
from stock_dashboard.analysis.indicators import add_indicators
from stock_dashboard.analysis.performance import performance_summary
from stock_dashboard.analysis.risk import risk_summary
from stock_dashboard.analysis.recommendations import build_market_commentary
from stock_dashboard.components.header import render_header
from stock_dashboard.components.sidebar import render_sidebar
from stock_dashboard.components.metrics import render_metrics
from stock_dashboard.components.price_chart import render_price_chart
from stock_dashboard.components.indicator_charts import render_indicator_charts
from stock_dashboard.components.summary import render_summary
from stock_dashboard.components.data_table import render_data_table
from stock_dashboard.utils.errors import MarketDataError

load_dotenv()
st.set_page_config(page_title=APP_TITLE, page_icon="📈", layout="wide")
render_header()

ticker, period, interval, submitted = render_sidebar(
    DEFAULT_TICKER, DEFAULT_PERIOD, PERIOD_OPTIONS
)

if submitted:
    try:
        service = MarketDataService()
        with st.spinner(f"Loading market data for {ticker.upper()}..."):
            raw = service.get_history(ticker, period, interval)
            if raw.empty:
                raise MarketDataError("No market data returned. Check the ticker symbol and try another period.")
            analyzed = add_indicators(raw)
            info = service.get_ticker_info(ticker)
            st.session_state["stock_analysis"] = {
                "ticker": ticker.upper(), "period": period, "interval": interval,
                "raw": raw, "data": analyzed, "info": info,
            }
    except MarketDataError as exc:
        st.error(str(exc))
        st.session_state.pop("stock_analysis", None)
    except Exception as exc:
        st.error(f"Unexpected error: {exc}")
        st.session_state.pop("stock_analysis", None)

state = st.session_state.get("stock_analysis")
if state:
    df, info = state["data"], state["info"]
    render_summary(state["ticker"], info, df)
    render_metrics(df, performance_summary(df), risk_summary(df))

    tab_price, tab_indicators, tab_analysis, tab_data = st.tabs(
        ["📈 Price chart", "🧮 Technical indicators", "🧠 Analysis", "📋 Historical data"]
    )
    with tab_price:
        render_price_chart(df, state["ticker"])
    with tab_indicators:
        render_indicator_charts(df)
    with tab_analysis:
        commentary = build_market_commentary(df)
        st.subheader("Rule-based market commentary")
        st.info(commentary["overview"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Trend signal", commentary["trend"])
        c2.metric("Momentum signal", commentary["momentum"])
        c3.metric("Volatility", commentary["volatility"])
        st.caption("These descriptive signals are based on historical indicators. They are not personalized investment advice or guaranteed predictions.")
    with tab_data:
        render_data_table(df, state["ticker"])
else:
    st.info("Choose a ticker in the sidebar and click **Analyze stock**.")
    st.markdown("### Dashboard modules")
    a, b, c, d = st.columns(4)
    a.markdown("**Price history**\n\nCandlesticks, volume and moving averages.")
    b.markdown("**Indicators**\n\nRSI, MACD, Bollinger Bands and SMA.")
    c.markdown("**Performance**\n\nReturns, drawdown and volatility metrics.")
    d.markdown("**Data export**\n\nDownload historical data as CSV.")
    st.caption("Market data is supplied by Yahoo Finance through yfinance. Availability and delay depend on the instrument and data provider.")
