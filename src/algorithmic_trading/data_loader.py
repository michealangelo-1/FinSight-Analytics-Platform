import yfinance as yf

def download_data():

    data = yf.download(
        "AAPL",
        start="2020-01-01",
        end="2025-01-01",
        auto_adjust=True
    )

    data.columns = [
        col[0] if isinstance(col, tuple) else col
        for col in data.columns
    ]

    data.to_csv("data/market_data.csv")

    return data


if __name__ == "__main__":

    import os

    print("Current Working Directory:")
    print(os.getcwd())

    df = download_data()

    print(df.head())