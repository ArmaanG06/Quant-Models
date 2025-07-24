import math
from scipy.stats import norm

def d1(S: float, K: float, T: float, r:float, sigma: float) -> float:
    """
    Calculate d1 used in Black-Scholes model
    """
    return (math.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

def d2 (S:float, K:float, T:float, r:float, sigma:float) -> float:
    """
    Calculate d2 used in black-scholes model
    """
    return d1(S,K,T,r,sigma) - sigma * math.sqrt(T)

def black_scholes_price(S: float, K:float, T: float, r: float, sigma: float, option_type: str='call') -> float:
    """
    Price a European option using the Black-Scholes formula.

    Parameters:
        S: Spot price of the underlying
        K: Strike price
        T: Time to maturity in years
        r: Risk-free interest rate (annualized)
        sigma: Volatility of the underlying (annualized std dev)
        option_type: 'call' or 'put'

    Returns:
        Option price (float)
    """
    if T<=0 or sigma <= 0 or S <= 0 or K <= 0:
        raise ValueError("Invalid input: ensure S, K, T, sigma > 0")
    
    d_1 = d1( S, K, T, r , sigma)
    d_2 = d2( S, K, T, r , sigma)

    if option_type == 'call':
        price = S * norm.cdf(d_1) - K * math.exp(-r * T) * norm.cdf (d_2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d_2) - S * norm.cdf(-d_1)
    else:
        raise ValueError("Invalid option_type. Must be 'call' or 'put'")
    
    return price