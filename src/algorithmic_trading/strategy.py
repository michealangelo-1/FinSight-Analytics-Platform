import pandas as pd 

def create_signals():
    df = pd.read_csv("data/market_data.csv")

    df["MA50"] = df["Close"].rolling(window=50).mean()
    df["MA200"] = df["Close"].rolling(window=200).mean()

    df["Signal"] = 0
    df.loc[df['MA50'] > df['MA200'], "Signal"] = 1

    df.to_csv("data/trading_signals.csv", index=False)

    return df

if __name__ == "__main__":

    signals = create_signals()

    print(
        signals[
            ["Date", "Close","MA50", "MA200", "Signal"]
        ].tail()
    )
