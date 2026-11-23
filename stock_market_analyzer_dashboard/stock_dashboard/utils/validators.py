import re

TICKER_PATTERN = re.compile(r"^[A-Za-z0-9.^=_-]{1,25}$")

def is_valid_ticker(ticker):
    return bool(TICKER_PATTERN.fullmatch((ticker or "").strip()))
