import pandas as pd
from stock_dashboard.analysis.performance import performance_summary

def test_performance_summary():
    frame = pd.DataFrame({"Close": [100.0, 110.0, 105.0]})
    result = performance_summary(frame)
    assert round(result["period_return"], 4) == 0.05
    assert result["best_day"] > 0
    assert result["worst_day"] < 0
