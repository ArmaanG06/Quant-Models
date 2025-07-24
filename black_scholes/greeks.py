import math
from scipy.stats import norm
from bs_formula import d1, d2

def delta(S, K, T, r, sigma, option_type='call'):
    d_1 = d1(S, K, T, r, sigma)
    if option_type == 'call':
        return norm.cdf(d_1)
    elif option_type == 'put':
        return norm.cdf(d_1) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def gamma(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return norm.pdf(d_1) / (S * sigma * math.sqrt(T))

def vega(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(d_1) * math.sqrt(T) / 100  # per 1% change

def theta(S, K, T, r, sigma, option_type='call'):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)

    term1 = - (S * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T))
    if option_type == 'call':
        term2 = r * K * math.exp(-r * T) * norm.cdf(d_2)
        return (term1 - term2) / 365  # per day
    elif option_type == 'put':
        term2 = r * K * math.exp(-r * T) * norm.cdf(-d_2)
        return (term1 + term2) / 365  # per day
    else:
        raise ValueError("option_type must be 'call' or 'put'")

def rho(S, K, T, r, sigma, option_type='call'):
    d_2 = d2(S, K, T, r, sigma)
    if option_type == 'call':
        return K * T * math.exp(-r * T) * norm.cdf(d_2) / 100  # per 1% change
    elif option_type == 'put':
        return -K * T * math.exp(-r * T) * norm.cdf(-d_2) / 100  # per 1% change
    else:
        raise ValueError("option_type must be 'call' or 'put'")
