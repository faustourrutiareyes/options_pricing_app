# Interactive Financial Modeling Dashboard with Monte Carlo Simulation
[Link to the UI](https://faustourrutiareyes-options-simulator.share.connect.posit.cloud)
![image](https://github.com/user-attachments/assets/790aa39c-fa4b-4d91-804b-22b3ad1ad5ca)

This project is an interactive financial modeling dashboard that utilizes Monte Carlo simulations to model stock price movements and option pricing. The dashboard is built using Shiny for Python and allows users to fetch real-time stock data, simulate stock price paths based on Geometric Brownian Motion, and calculate option premiums for various strike prices.

## Features
- Monte Carlo Simulation for Asset Pricing:
Simulate multiple stock price paths using Geometric Brownian Motion to model future stock prices based on historical volatility and risk-free interest rates.

- Option Pricing Calculator:
Calculate the option premium for a given strike price using real-time data and established financial models.

- Real-Time Data Fetching:
The dashboard allows users to input a stock ticker and fetch up-to-date market data using reliable sources like Yahoo Finance or other financial APIs.

- Interactive Visualizations:
The dashboard provides dynamic visualizations of simulated stock price paths and option pricing data. Users can compare multiple paths and assess risk.

- Real-Time Option Pricing:
Users can calculate option premiums based on Black-Scholes or other option pricing models, taking into account live market conditions.

## Technologies Used
- Python:
The core of the project is developed using Python, utilizing libraries like NumPy for numerical computations and Shiny for Python for creating the interactive dashboard.

- Shiny for Python:
A powerful library that allows the development of interactive web applications directly from Python code, making it easy to create the dashboard.

- NumPy:
Used for efficient array-based calculations and simulations, particularly for the Monte Carlo simulations.

- Financial Data APIs:
Integrated with Yahoo Finance (or other APIs) to fetch real-time stock data and option-related information.

- Matplotlib/Plotly:
For interactive and visually appealing charts, including the visualization of stock price paths and option pricing.


## How to Use
1. Input Stock Ticker:
Enter the stock ticker symbol (e.g., AAPL, TSLA, etc.) into the provided input field to fetch the latest market data.

2. Simulate Stock Price:
Adjust the volatility and time horizon parameters to simulate potential future stock price movements using Monte Carlo simulations.

3. Option Pricing:
Enter a strike price and select an option type (call or put) to calculate the option premium using the Black-Scholes model or any other model implemented.

4. Visualization:
The simulated stock price paths and option pricing graphs will be displayed dynamically as you adjust the parameters. You can compare different paths and analyze their implications on the portfolio.
Advanced Option Pricing Models: Implement additional option pricing models (e.g., Binomial Tree, Monte Carlo for American options).
Portfolio Optimization: Add portfolio optimization tools based on Markowitz Efficient Frontier or Modern Portfolio Theory (MPT).
Machine Learning: Integrate machine learning models for stock price prediction using historical data.
Multiple Ticker Support: Allow users to input multiple tickers and perform simulations and analysis for a diversified portfolio.
Risk Analysis: Implement features for Value-at-Risk (VaR) and Stress Testing based on the simulated stock paths.
