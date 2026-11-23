from stock_dashboard.utils.validators import is_valid_ticker

def test_valid_tickers():
    assert is_valid_ticker("AAPL")
    assert is_valid_ticker("RELIANCE.NS")
    assert is_valid_ticker("^NSEI")

def test_invalid_tickers():
    assert not is_valid_ticker("")
    assert not is_valid_ticker("ticker with spaces")
