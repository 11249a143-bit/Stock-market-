import pandas as pd

def performance_summary(df):
    close = df["Close"].dropna()
    if len(close) < 2:
        return {"period_return": 0.0, "best_day": 0.0, "worst_day": 0.0}
    returns = close.pct_change().dropna()
    return {
        "period_return": float(close.iloc[-1] / close.iloc[0] - 1),
        "best_day": float(returns.max()) if not returns.empty else 0.0,
        "worst_day": float(returns.min()) if not returns.empty else 0.0,
    }

def annualized_return(df, periods_per_year=252):
    returns = df["Close"].pct_change().dropna()
    if returns.empty:
        return 0.0
    years = len(returns) / periods_per_year
    if years <= 0:
        return 0.0
    growth = float((1 + returns).prod())
    return growth ** (1 / years) - 1 if growth > 0 else -1.0
