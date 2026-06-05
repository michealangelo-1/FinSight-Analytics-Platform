import pandas as pd

import numpy as np

from data_loader import load_data as get_stock_data

from metrics import (
    calculate_daily_returns,
    calculate_average_return,
    calculate_volatility,
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

from visualizations import (
    plot_portfolio_returns,
    plot_cumulative_growth,
    plot_risk_return
)

stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

data = get_stock_data(
    stocks,
    "2022-01-01",
    "2025-01-01"
)

returns = calculate_daily_returns(data)

average_return = calculate_average_return(returns)
volatility = calculate_volatility(returns)

weights = np.array([0.20, 0.20, 0.20, 0.20, 0.20])

portfolio_return = calculate_portfolio_return(
    returns,
    weights
)

portfolio_volatility = calculate_portfolio_volatility(
    portfolio_return
)

sharpe_ratio = calculate_sharpe_ratio(
    portfolio_return
)

max_drawdown = calculate_max_drawdown(
    portfolio_return
)

metrics_df = pd.DataFrame({
    "Average Return": average_return,
    "Volatility": volatility
})

metrics_df.to_csv(
    "reports/portfolio_metrics.csv"
)

portfolio_summary = pd.DataFrame({
    "Metrics": [
        "Portfolio Volatility",
        "Sharpe Ratio",
        "Maximum Drawdown"
    ],
    "Value": [
        portfolio_volatility,
        sharpe_ratio,
        max_drawdown
    ]
})

portfolio_summary.to_csv(
    "reports/portfolio_summary.csv",
    index=False
)
    

print("Prices:")
print(data.head())

print("\nDaily Returns:")
print(returns.head())

print("\nAverage Daily Return:")
print(average_return)

print("\nVolatility:")
print(volatility)

print("\nPortfolio Daily Return:")
print(portfolio_return.head())

print("\nPortfolio Volatility:")
print(portfolio_volatility)

print("\nSharpe Ratio:")
print(sharpe_ratio)

print("\nMax Drawdown:")
print(max_drawdown)

plot_portfolio_returns(portfolio_return)
plot_cumulative_growth(portfolio_return)
plot_risk_return(
    average_return,
    volatility
)