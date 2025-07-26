import numpy as np

def generate_gbm_paths(S0, T, r, sigma, n_steps, n_paths, seed=None):
    """
    Simulate GBM price paths.

    Parameters:
        S0 (float): Initial stock price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate
        sigma (float): Volatility (annualized)
        n_steps (int): Number of time steps
        n_paths (int): Number of simulation paths
        seed (int): Random seed for reproducibility

    Returns:
        np.ndarray: Simulated price paths of shape (n_paths, n_steps+1)
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / n_steps
    time_grid = np.linspace(0, T, n_steps + 1)

    # Generate random Brownian increments
    Z = np.random.standard_normal((n_paths, n_steps))
    W = np.cumsum(Z * np.sqrt(dt), axis=1)

    # Apply GBM formula
    drift = (r - 0.5 * sigma ** 2) * time_grid[1:]  # Skip t=0
    diffusion = sigma * W

    log_paths = np.zeros((n_paths, n_steps + 1))
    log_paths[:, 0] = np.log(S0)
    log_paths[:, 1:] = np.log(S0) + drift + diffusion

    return np.exp(log_paths)
