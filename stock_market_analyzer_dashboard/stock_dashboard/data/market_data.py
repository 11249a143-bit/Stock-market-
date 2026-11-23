import pandas as pd

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]

def normalize_history(frame):
    if frame is None or frame.empty:
        return pd.DataFrame(columns=REQUIRED_COLUMNS)
    df = frame.copy()
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.loc[:, ~df.columns.duplicated()]
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required market data columns: {', '.join(missing)}")
    df = df[REQUIRED_COLUMNS].copy()
    df.index = pd.to_datetime(df.index)
    df = df.sort_index().dropna(subset=["Close"])
    for column in REQUIRED_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    return df.dropna(subset=["Open", "High", "Low", "Close"])
