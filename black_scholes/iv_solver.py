
from scipy.stats import norm
from bs_formula import black_scholes_price
import math

def implied_volatility(S, K, T, r, market_price, option_type='call', method='newton', tol=1e-6, max_iter=100) -> float:
    """
    Estimate implied volatility from a market option price.

    Parameters:
        S: Spot price
        K: Strike price
        T: Time to maturity (in years)
        r: Risk-free rate
        market_price: Observed market price of the option
        option_type: 'call' or 'put'
        method: 'newton' or 'bisection'
        tol: Tolerance for convergence
        max_iter: Maximum number of iterations

    Returns:
        Estimated implied volatility
    """
    if method == 'newton':
        return _newton_iv(S, K, T, r, market_price, option_type, tol, max_iter)
    elif method == 'bisection':
        return _bisection_iv(S, K, T, r, market_price, option_type, tol, max_iter)
    else:
        raise ValueError("Invalid method: choose 'newton' or 'bisection'")

def _newton_iv(S, K, T, r, market_price, option_type, tol, max_iter):
    from greeks import vega  # Use analytical vega

    sigma = 0.2  # Initial guess

    for i in range(max_iter):
        price = black_scholes_price(S, K, T, r, sigma, option_type)
        v = vega(S, K, T, r, sigma)

        if v < 1e-8:
            break  # Avoid divide by zero or flat vega

        diff = price - market_price
        if abs(diff) < tol:
            return sigma

        sigma -= diff / (v * 100)  # Because vega is per 1% change

    # If Newton fails, fall back
    return _bisection_iv(S, K, T, r, market_price, option_type, tol, max_iter)

def _bisection_iv(S, K, T, r, market_price, option_type, tol, max_iter):
    low = 1e-6
    high = 5.0

    for i in range(max_iter):
        mid = (low + high) / 2
        price = black_scholes_price(S, K, T, r, mid, option_type)

        if abs(price - market_price) < tol:
            return mid

        if price > market_price:
            high = mid
        else:
            low = mid

    return (low + high) / 2
