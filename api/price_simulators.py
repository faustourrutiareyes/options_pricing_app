import numpy as np
from scipy.stats import norm

def black_scholes(S0, K, T, r, sigma, option_type="call"):
    """
    Compute the Black-Scholes price for a European call or put option.

    Parameters:
    S0 : float  - Initial stock price
    K  : float  - Strike price
    T  : float  - Time to expiration (in years)
    r  : float  - Risk-free interest rate (annualized)
    sigma : float - Volatility of the stock (annualized)
    option_type : str - "call" for call option, "put" for put option

    Returns:
    float - Option price
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    return price

def simulate_stock_paths(S0: float, T: int, r: float, sigma: float, num_paths: int = 5, steps_per_year: int = 252):
    """
    Simulate the possible paths of an assets following Geometric Brownian Motion

    Parameters:
    S0 : float  - Initial stock price
    T  : float  - Time to expiration (in years)
    r  : float  - Risk-free interest rate (annualized)
    sigma : float - Volatility of the stock (annualized)
    num_paths : int - The number of paths to simulate
    steps_per_year : int - The days in a trading year

    Returns:
    list - The paths simulated 
    """
    num_steps = int(T * steps_per_year)
    dt = 1 / steps_per_year
    paths = np.zeros((num_steps + 1, num_paths))
    paths[0] = S0

    for t in range(1, num_steps + 1):
        Z = np.random.standard_normal(num_paths)
        paths[t] = paths[t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return paths