def format_currency(value, currency=""):
    try:
        return f"{currency} {float(value):,.2f}".strip()
    except (TypeError, ValueError):
        return "N/A"

def format_percent(value):
    try:
        return f"{float(value):+.2%}"
    except (TypeError, ValueError):
        return "N/A"
