import yfinance as yf


def load_data(tickers, start, end):
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True
    )

    return data["Close"]