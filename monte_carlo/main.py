# main.py

from simulate_paths import generate_gbm_paths
from option_pricing import monte_carlo_option_price
from visualizations import plot_paths, plot_terminal_distribution, plot_payoff_distribution

def main():
    # === Parameters ===
    S0 = 100           # Initial price
    K = 100            # Strike price
    T = 1.0            # Time to maturity (1 year)
    r = 0.05           # Risk-free rate
    sigma = 0.2        # Volatility (20%)
    n_steps = 252      # Time steps (daily)
    n_paths = 10000    # Number of Monte Carlo paths
    seed = 42          # Random seed for reproducibility

    # === Step 1: Simulate GBM paths ===
    paths = generate_gbm_paths(S0, T, r, sigma, n_steps, n_paths, seed=seed)

    # === Step 2: Monte Carlo Option Pricing ===
    call_price = monte_carlo_option_price(paths, K, r, T, option_type='call')
    put_price  = monte_carlo_option_price(paths, K, r, T, option_type='put')

    print("==== Monte Carlo Option Pricing ====")
    print(f"Call Option Price: {call_price:.4f}")
    print(f"Put Option Price:  {put_price:.4f}")

    # === Step 3: Visualizations ===
    plot_paths(paths, n_samples=20)
    plot_terminal_distribution(paths)
    plot_payoff_distribution(paths, K, r, T, option_type='call')
    plot_payoff_distribution(paths, K, r, T, option_type='put')

if __name__ == "__main__":
    main()
