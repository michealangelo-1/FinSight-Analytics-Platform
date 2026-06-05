import numpy as np


def calculate_daily_returns(prices):
    return prices.pct_change().dropna()


def calculate_average_return(returns):
    return returns.mean()


def calculate_volatility(returns):
    return returns.std()


def calculate_portfolio_return(returns, weights):
    return returns.dot(weights)


def calculate_portfolio_volatility(portfolio_returns):
    return portfolio_returns.std()


def calculate_sharpe_ratio(portfolio_return, risk_free_rate=0):
    excess_return = portfolio_return - risk_free_rate
    return excess_return.mean() / excess_return.std()


def calculate_max_drawdown(portfolio_returns):
    cumulative_returns = (1 + portfolio_returns).cumprod()

    running_max = cumulative_returns.cummax()

    drawdown = (
        cumulative_returns - running_max
    ) / running_max

    return drawdown.min()