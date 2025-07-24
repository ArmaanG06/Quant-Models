# main.py

from bs_formula import black_scholes_price
from greeks import delta, gamma, vega, theta, rho
from iv_solver import implied_volatility

def run_demo():
    # Sample option parameters
    S = 100        # Spot price
    K = 100        # Strike price
    T = 1          # Time to maturity (1 year)
    r = 0.05       # Risk-free rate
    sigma = 0.2    # Volatility
    option_type = 'call'
    market_price = 10.5

    print("==== Black-Scholes Model ====")
    price = black_scholes_price(S, K, T, r, sigma, option_type)
    print(f"{option_type.capitalize()} Option Price: {price:.4f}")

    print("\n---- Greeks ----")
    print(f"Delta: {delta(S, K, T, r, sigma, option_type):.4f}")
    print(f"Gamma: {gamma(S, K, T, r, sigma):.4f}")
    print(f"Vega:  {vega(S, K, T, r, sigma):.4f}")
    print(f"Theta: {theta(S, K, T, r, sigma, option_type):.4f}")
    print(f"Rho:   {rho(S, K, T, r, sigma, option_type):.4f}")

    print("\n---- Implied Volatility ----")
    iv = implied_volatility(S, K, T, r, market_price, option_type)
    print(f"Implied Volatility (from market price {market_price}): {iv:.4f}")

if __name__ == "__main__":
    run_demo()
