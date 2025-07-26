# main.py (super directory)

from black_scholes.bs_formula import black_scholes_price
from monte_carlo.simulate_paths import generate_gbm_paths
from monte_carlo.option_pricing import monte_carlo_option_price

def main():
    # === Common Option Parameters ===
    S = 100         # Spot price
    K = 100         # Strike price
    T = 1.0         # Time to maturity (years)
    r = 0.05        # Risk-free rate
    sigma = 0.2     # Volatility
    option_type = 'call'

    print("=== Option Pricing Comparison ===")
    print(f"Underlying: {S}, Strike: {K}, T: {T}, r: {r}, σ: {sigma}, Type: {option_type}")

    # === Black-Scholes Analytical Price ===
    bs_price = black_scholes_price(S, K, T, r, sigma, option_type)
    print(f"[Black-Scholes] Price: {bs_price:.4f}")

    # === Monte Carlo Simulation Price ===
    n_paths = 10000
    n_steps = 252
    seed = 42

    paths = generate_gbm_paths(S, T, r, sigma, n_steps, n_paths, seed)
    mc_price = monte_carlo_option_price(paths, K, r, T, option_type)
    print(f"[Monte Carlo]   Price: {mc_price:.4f}")

    # === Price Difference ===
    diff = abs(bs_price - mc_price)
    print(f"Difference: {diff:.4f}")

if __name__ == "__main__":
    main()
