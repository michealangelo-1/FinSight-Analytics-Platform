# FinSight Analytics Platform

## Project Roadmap

### Completed Modules

- ✅ Module 1: Credit Risk Prediction
- ✅ Module 2: Portfolio Analytics
- ✅ Module 3: Algorithmic Trading Strategy Backtesting
- ✅ Module 4: Fraud Detection System
- ✅ Module 5: Financial Forecasting & Time Series Analysis

### Upcoming Modules


- ⬜ Module 6: Stock Valuation Engine (DCF & Multiples)


## Module 1: Credit Risk Prediction


### Overview

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



## Module 4: Fraud Detection System

### Overview

Built a machine learning system to identify fraudulent credit card transactions using historical transaction data.

### Techniques Used

- Exploratory Data Analysis
- Class Imbalance Analysis
- Random Forest Classification
- ROC Curve Evaluation
- Feature Importance Analysis

### Outputs

- Confusion Matrix
- ROC Curve
- Feature Importance Visualization

### Skills Demonstrated

- Fraud Analytics
- Machine Learning
- Classification Modeling
- Financial Risk Management


### Dataset

The Credit Card Fraud Detection dataset is not included in this repository due to GitHub file size limitations.

Download the dataset separately and place it in:

data/creditcard.csv



# Module 5: Financial Forecasting & Time Series Analysis

### Overview

This module focuses on forecasting stock prices using historical market data and time series modeling techniques.

## Objectives

- Download historical stock data using Yahoo Finance
- Perform exploratory time series analysis
- Generate moving average indicators
- Build an ARIMA forecasting model
- Evaluate forecasting performance using MAE and RMSE
- Visualize actual vs predicted stock prices

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- yFinance
- Scikit-learn

## Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Analysis
4. Feature Engineering
5. ARIMA Modeling
6. Forecast Evaluation
7. Visualization

## Results

Model Performance:

- MAE: 25.14
- RMSE: 29.64

## Generated Outputs

### Charts

- Closing Price Trend
- Moving Averages
- Actual vs Predicted Forecast

### Forecast Files

- forecast_metrics.csv
- forecast_results.csv

## Skills Demonstrated

- Time Series Analysis
- Financial Forecasting
- Statistical Modeling
- Data Visualization
- Performance Evaluation