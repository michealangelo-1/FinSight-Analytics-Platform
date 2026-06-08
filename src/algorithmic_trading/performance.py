import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_performance():

    df = pd.read_csv("data/backtest_results.csv")

    strategy_returns = df["Strategy_Return"].dropna()

    total_return = (
        df["Cumulative_Strategy"].iloc[-1] - 1
    )

    annual_return = (
        (1 + total_return)
        **(252 / len(strategy_returns))
        - 1
    )

    volatility = (
        strategy_returns.std()
        * np.sqrt(252)
    )

    sharpe_ratio = (
        annual_return / volatility
        if volatility != 0
        else 0
    )

    rolling_max = (
        df["Cumulative_Strategy"].cummax()
    )

    drawdown = (
        df["Cumulative_Strategy"]
        / rolling_max
        - 1
    )

    max_drawdown = drawdown.min()

    metrics = pd.DataFrame({
        "Metrics": [
            "Total Return",
            "Annual Return",
            "Volatility",
            "Sharpe Ratio",
            "Maximum Drawdown"
        ],
        "Value": [
            total_return,
            annual_return,
            volatility,
            sharpe_ratio,
            max_drawdown
        ]
    })

    metrics.to_csv(
        "outputs/performance_metrics.csv",
        index=False
    )

    print(metrics)

    return metrics

def plot_equity_curve():

    df = pd.read_csv("data/backtest_results.csv")

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Cumulative_Market"],
        label="Buy & Hold"
    )

    plt.plot(
        df["Cumulative_Strategy"],
        label="Strategy"
    )

    plt.title("Strategy vs Buy & Hold")
    plt.xlabel("Trading Days")
    plt.ylabel("Portfolio Growth")
    plt.legend()

    plt.savefig(
        "outputs/equity_curve.png"
    )

def plot_drawdown():

    df = pd.read_csv("data/backtest_results.csv")

    rolling_max = (
        df["Cumulative_Strategy"]
        .cummax()
    )  

    drawdown = (
        df["Cumulative_Strategy"]
        / rolling_max
        - 1
    )

    plt.figure(figsize=(10, 6))

    plt.plot(drawdown)

    plt.title("Strategy Drawdown")
    plt.xlabel("Trading Days")
    plt.ylabel("Drawdown")

    plt.savefig(
        "outputs/drawdown_chart.png"
    )

plt.show()


if __name__ == "__main__":
    calculate_performance()

    plot_equity_curve()

    plot_drawdown()