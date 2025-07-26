# visualizations.py
import matplotlib.pyplot as plt
import numpy as np

def plot_paths(paths, n_samples=10, title='Simulated Price Paths'):
    """
    Plot a few sample simulated price paths.
    
    Parameters:
        paths (np.ndarray): GBM paths, shape (n_paths, n_steps+1)
        n_samples (int): Number of paths to plot
        title (str): Plot title
    """
    plt.figure(figsize=(10, 5))
    for i in range(min(n_samples, paths.shape[0])):
        plt.plot(paths[i], lw=1)
    plt.title(title)
    plt.xlabel("Time Steps")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()

def plot_terminal_distribution(paths, bins=50):
    """
    Plot the histogram of final prices (S_T).
    
    Parameters:
        paths (np.ndarray): GBM paths
        bins (int): Histogram bins
    """
    S_T = paths[:, -1]
    plt.figure(figsize=(8, 4))
    plt.hist(S_T, bins=bins, alpha=0.7, color='steelblue', edgecolor='black')
    plt.title("Distribution of Final Prices (S_T)")
    plt.xlabel("Price at Maturity")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_payoff_distribution(paths, K, r, T, option_type='call', bins=50):
    """
    Plot histogram of option payoffs at maturity.
    
    Parameters:
        paths (np.ndarray): GBM paths
        K (float): Strike price
        r (float): Risk-free rate
        T (float): Time to maturity
        option_type (str): 'call' or 'put'
        bins (int): Histogram bins
    """
    S_T = paths[:, -1]
    if option_type == 'call':
        payoffs = np.maximum(S_T - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

    discounted_payoffs = np.exp(-r * T) * payoffs

    plt.figure(figsize=(8, 4))
    plt.hist(discounted_payoffs, bins=bins, alpha=0.7, color='darkorange', edgecolor='black')
    plt.title(f"Discounted {option_type.capitalize()} Payoff Distribution")
    plt.xlabel("Payoff")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
