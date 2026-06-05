import matplotlib.pyplot as plt


def plot_portfolio_returns(portfolio_returns):
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_returns.index, portfolio_returns)
    plt.title("Portfolio Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.grid(True)
    plt.show()


def plot_cumulative_growth(portfolio_returns):
    cumulative_growth = (1 + portfolio_returns).cumprod()

    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_growth.index, cumulative_growth)
    plt.title("Portfolio Growth Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()


def plot_risk_return(avg_returns, volatility):
    plt.figure(figsize=(10, 6))

    plt.scatter(volatility, avg_returns)

    for stock in avg_returns.index:
        plt.annotate(
            stock,
            (volatility[stock], avg_returns[stock])
        )

    plt.xlabel("Risk (Volatility)")
    plt.ylabel("Average Return")
    plt.title("Risk vs Return")
    plt.grid(True)
    plt.show()