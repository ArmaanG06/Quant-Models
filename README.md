# Quantitative Option Pricing Models 📈

A modular Python project implementing both **Black-Scholes** and **Monte Carlo simulation** methods for pricing European options. Designed to demonstrate theoretical understanding, numerical techniques, and practical coding ability — all in one cohesive quant-dev toolkit.

---

## Project Overview

This project consists of two independent, production-ready pricing engines:

| Module | Description |
|--------|-------------|
| `black_scholes/` | Analytical pricing using the Black-Scholes model, including Greeks and implied volatility solver |
| `monte_carlo/`   | Simulation-based pricing using Geometric Brownian Motion and Monte Carlo techniques |

These modules are testable, extensible, and suitable for integration into larger trading or research systems.

---

## File Structure

```bash
quant_models/
├── black_scholes/          # Black-Scholes pricing engine
│   ├── bs_formula.py       # Core pricing functions
│   ├── greeks.py           # Delta, gamma, theta, vega, rho
│   ├── iv_solver.py        # Implied volatility via bisection
│   └── main.py             # Local module runner
│
├── monte_carlo/            # Monte Carlo simulation engine
│   ├── simulated_paths.py  # GBM path generator
│   ├── option_pricing.py   # MC option pricer
│   ├── visualizations.py   # Charts and distributions
│   └── main.py             # Local module runner
│
└── main.py                 # Master script comparing BS vs MC
```
## Features

- Black-Scholes pricing for European calls'puts
- Full greek calculation (delta, gamma, vega, theta, rho)
- Implied volatility estimation (numerical root-finding)
- Monte Carlo pricing using GBM
- Visualization of paths, payoffs, and terminal distributions\
- Comparison of MC vs analytical pricing
- Modular structure for future reuse or integration
- Tested and reproducible

## Sample Output

```bash
=== Option Pricing Comparison ===
Underlying: 100, Strike: 100, T: 1.0, r: 0.05, σ: 0.2, Type: call
[Black-Scholes] Price: 10.4506
[Monte Carlo]   Price: 10.2211
Difference: 0.2295
```
Plots generated include:
- Simulated price paths
- Final price distribution (S_T)
- Discounted payoff histograms

## Setup Instructions

1. Clone Repo
```bash
git clone https://github.com/ArmaanG06/Quant-Models
cd Quant-Models
```

2. Create Venv
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run Master Script
```bash
python main.py
```

## Educational Goals
This project was designed to:
- Demonstrate practical knowledge of option pricing theory
- Showcase numerical modeling and vectorized simulations
- Serve as a launchpad for more advanced quant work (vol surfaces, exotic options, real-market data integration)

## Author
Armaan G.
Student of Business & Computer Science
Aspiring Quant Developer / Trader
Linkedin: https://www.linkedin.com/in/armaan-gandhara/
Github: https://github.com/ArmaanG06
