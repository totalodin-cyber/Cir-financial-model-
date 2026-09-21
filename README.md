### Cox-Ingersoll-Ross (CIR) Interest Rate Model

I developed an implementation of the famous **Cox-Ingersoll-Ross (CIR) model** to analyze how short- and medium-term interest rates evolve. This project provides a framework to better understand the underlying dynamics, volatility, and structural composition of interest rates. 

Key Features & Methodology

Mean Reversion Dynamic (k and θ):** The model estimates the speed of mean reversion (k) using the covariance and variance of a one-year historical dataset with daily frequency.
The Long-Term Equilibrium (θ):** Instead of using a simple sample mean, the model calibrates θ conditional on the speed of adjustment (k). In financial literature, this is the preferred approach because a standard sample mean does not account for the continuous time-series gravity effect (the velocity at which rates are dragged back to their baseline).

Feller's Condition:** The script automatically validates the parameters using Feller's condition (2kθ ≥ σ²). This mathematical check ensures that simulated interest rates remain strictly positive, confirming the model's reliability for simulation purposes.

Parameter Annualization:** Since financial markets operate on daily data (252 trading days per year), the script standardizes the daily outputs into annualized terms, scaling both the speed of reversion (k) and the volatility (σ) to align with standard macroeconomic analysis.

### Market Outlook & Discretion

Based on the calibrated historical data, the model identifies a structural upward bias in current interest rates, suggesting room for growth. However, given the low speed of adjustment, the model implies that any transition toward the long-term equilibrium will be a gradual, multi-year process rather than an abrupt shift. 

Quantitative models are tools for risk management and scenario analysis, not crystal balls. As the old market adage goes: *"Only time will tell."*
