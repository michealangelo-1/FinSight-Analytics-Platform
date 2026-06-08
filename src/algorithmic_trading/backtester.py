import pandas as pd

def backtest_strategy():

    df = pd.read_csv("data/trading_signals.csv")

    df["Market_Return"] = df["Close"].pct_change()
    
    df["Strategy_Return"] = (
        df["Signal"].shift(1) * df["Market_Return"]
    )

    df["Cumulative_Market"] = (
        1 + df["Market_Return"]
    ).cumprod()

    df["Cumulative_Strategy"] = (
        1 + df["Strategy_Return"]
    ).cumprod()

    df.to_csv("data/backtest_results.csv", index=False)

    return df

if __name__ == "__main__":
    results = backtest_strategy()

    print(
        results[
            [
                "Date",
                "Cumulative_Market",
                "Cumulative_Strategy"
            ]
        ].tail()
    )