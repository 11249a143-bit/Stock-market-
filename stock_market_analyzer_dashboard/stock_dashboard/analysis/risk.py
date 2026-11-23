import numpy as np

def risk_summary(df, periods_per_year=252):
    returns = df["Close"].pct_change().dropna()
    if returns.empty:
        return {"volatility": 0.0, "max_drawdown": 0.0}
    volatility = float(returns.std() * np.sqrt(periods_per_year))
    wealth = (1 + returns).cumprod()
    drawdown = wealth / wealth.cummax() - 1
    return {
        "volatility": volatility,
        "max_drawdown": float(drawdown.min()),
    }
