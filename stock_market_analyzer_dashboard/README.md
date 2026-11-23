# Stock Market Analyzer Dashboard

A modular Streamlit stock dashboard built with Python, yfinance, pandas, ta and Plotly.

## Features
- Historical OHLCV data and candlestick chart
- SMA 20/50/200 and EMA 20
- RSI 14, MACD and Bollinger Bands
- Volume chart
- Period return, best/worst daily return, annualized volatility and maximum drawdown
- Rule-based descriptive market commentary
- Historical data table and CSV export
- Support for common US and Indian ticker formats
- Modular architecture and unit tests

## Requirements
- Python 3.10+
- Internet connection

## Run in VS Code on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell blocks activation, run:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
Then activate the environment again.

Open the URL Streamlit prints, usually http://localhost:8501.

## Example tickers
- `AAPL`, `MSFT`, `NVDA` — US-listed examples
- `RELIANCE.NS`, `TCS.NS`, `INFY.NS` — NSE examples
- `^NSEI` — NIFTY 50 index (provider availability may vary)

## Tests
```powershell
pytest
```

## Project layout
- `app.py`: Streamlit entry point
- `stock_dashboard/data`: market data normalization
- `stock_dashboard/services`: data provider and export functions
- `stock_dashboard/analysis`: indicators, performance, risk and commentary
- `stock_dashboard/components`: dashboard UI components
- `stock_dashboard/utils`: errors, formatters and ticker validation
- `pages`: About and methodology pages
- `tests`: basic unit tests

## Data and limitations
Data is downloaded from Yahoo Finance using the community-maintained yfinance package. Yahoo Finance availability, supported intervals, symbols and delays can change. This is not an official exchange feed. Some tickers may return no data. The dashboard uses adjusted historical prices and its simple annualized volatility calculation assumes daily observations; interpret results carefully for weekly or monthly intervals.

The rule-based commentary describes historical indicator readings. It is not a buy/sell recommendation, a forecast, or personalized financial advice. Historical performance does not predict future returns.
