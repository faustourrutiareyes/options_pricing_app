import yfinance as yf
import numpy as np

def ticker_info_call(ticker: str = "^TWII") -> tuple:
    # Fetch ticker data: by default Taiwan Weighted Index (^TWII)
    ticker_data = yf.Ticker(ticker)
    hist = ticker_data.history(period="1y")
    
    # Take last price of asset
    last_price = hist["Close"].iloc[-1]
    
    # Compute historical volatility (sigma)
    daily_returns = hist["Close"].pct_change().dropna()
    sigma = np.std(daily_returns) * np.sqrt(252)
    
    return last_price, sigma