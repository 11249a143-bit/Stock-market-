import yfinance as yf
import streamlit as st
from stock_dashboard.data.market_data import normalize_history
from stock_dashboard.utils.errors import MarketDataError

class MarketDataService:
    @staticmethod
    @st.cache_data(ttl=300, show_spinner=False)
    def _download(ticker, period, interval):
        try:
            history = yf.download(
                ticker, period=period, interval=interval,
                auto_adjust=True, progress=False, threads=False
            )
        except Exception as exc:
            raise MarketDataError(f"Yahoo Finance request failed: {exc}") from exc
        try:
            return normalize_history(history)
        except ValueError as exc:
            raise MarketDataError(str(exc)) from exc

    def get_history(self, ticker, period="1y", interval="1d"):
        symbol = ticker.strip().upper()
        if not symbol:
            raise MarketDataError("Enter a valid ticker symbol.")
        df = self._download(symbol, period, interval)
        if df.empty:
            raise MarketDataError(f"No data found for '{symbol}'. Verify the ticker and market.")
        return df

    @staticmethod
    @st.cache_data(ttl=900, show_spinner=False)
    def get_ticker_info(ticker):
        try:
            info = yf.Ticker(ticker).get_info()
            return info or {}
        except Exception:
            return {}
