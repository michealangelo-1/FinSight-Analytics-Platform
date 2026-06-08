# FinSight Analytics Platform


## Module 1: Credit Risk Prediction


## Project Overview

This project predicts loan approval status using machine learning.

## Dataset Features

- Income
- Loan Amount
- CIBIL Score
- Assets
- Education
- Employment Status

## Models Used

- Logistic Regression
- Random Forest

## Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 79.86% |
| Random Forest | 97.66% |

## Technologies

- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn

## Module 2: Portfolio Analytics

### Overview

Built a portfolio analytics system using Python and Yahoo Finance data.

### Features

* Multi-stock portfolio analysis
* Daily return calculations
* Volatility analysis
* Portfolio return computation
* Sharpe Ratio calculation
* Maximum Drawdown analysis
* Portfolio growth visualization
* Risk vs Return analysis
* CSV report generation

### Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Yahoo Finance (yfinance)

### Portfolio Assets

* Apple (AAPL)
* Microsoft (MSFT)
* Alphabet (GOOGL)
* Amazon (AMZN)
* Tesla (TSLA)

## Module 3: Algorithmic Trading Strategy Backtesting

### Overview

Built an algorithmic trading strategy using historical stock market data and moving average crossover signals. The strategy was backtested against a buy-and-hold benchmark to evaluate performance and risk.

### Features

* Historical stock market data retrieval using Yahoo Finance
* 50-Day Moving Average calculation
* 200-Day Moving Average calculation
* Trading signal generation (Golden Cross / Death Cross)
* Strategy backtesting framework
* Daily return calculation
* Cumulative return tracking
* Benchmark comparison against Buy-and-Hold
* Performance metric calculation
* Equity curve visualization
* Drawdown analysis
* CSV report generation

### Strategy Logic

**Buy Signal**

* 50-Day Moving Average > 200-Day Moving Average

**Sell Signal**

* 50-Day Moving Average < 200-Day Moving Average

### Performance Metrics

* Total Return
* Annualized Return
* Volatility
* Sharpe Ratio
* Maximum Drawdown

### Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Yahoo Finance (yFinance)

### Output Files

* market_data.csv
* trading_signals.csv
* backtest_results.csv
* performance_metrics.csv
* equity_curve.png
* drawdown_chart.png

### Learning Outcomes

* Financial market data handling
* Technical indicator implementation
* Trading signal generation
* Strategy backtesting
* Risk-adjusted performance evaluation
* Financial data visualization
* Quantitative finance fundamentals