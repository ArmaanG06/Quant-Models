import numpy as np

def monte_carlo_option_price(paths, K, r, T, option_type='call'):
    """
    Monte Carlo option pricing using simulated paths.

    Parameters:
        paths (np.ndarray): Simulated GBM paths, shape (n_paths, n_steps + 1)
        K (float): Strike price
        r (float): Risk-free interest rate
        T (float): Time to maturity (in years)
        option_type (str): 'call' or 'put'

    Returns:
        float: Estimated option price
    """
    S_T = paths[:, -1]  # Final price of each path

    if option_type == 'call':
        payoffs = np.maximum(S_T - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

    discounted_payoff = np.exp(-r * T) * payoffs
    return np.mean(discounted_payoff)
