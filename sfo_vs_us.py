import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the simulation
num_months = 24
initial_revenue = 20000  # Initial monthly revenue

# Growth rates for SaaS startup
saas_sf_growth_rates = [0.25, 0.15, 0.08]  # SF Bay Area
saas_us_growth_rates = [0.10, 0.05, 0.02]  # Nationwide US

# Growth rates for Education startup
edu_sf_growth_rates = [0.20, 0.10, 0.05]  # SF Bay Area
edu_us_growth_rates = [0.08, 0.04, 0.02]  # Nationwide US

# Growth rates for General startup
gen_sf_growth_rates = [0.15, 0.10, 0.05]  # SF Bay Area
gen_us_growth_rates = [0.05, 0.03, 0.01]  # Nationwide US

def simulate_revenue(initial_revenue, growth_rates, num_months):
    revenue = np.zeros(num_months)
    for month in range(num_months):
        if month == 0:
            revenue[month] = initial_revenue
        elif month < 6:
            revenue[month] = revenue[month - 1] * (1 + growth_rates[0])
        elif month < 18:
            revenue[month] = revenue[month - 1] * (1 + growth_rates[1])
        else:
            revenue[month] = revenue[month - 1] * (1 + growth_rates[2])
    return revenue

# Simulate revenue for each scenario
months = np.arange(1, num_months + 1)
revenue_saas_sf = simulate_revenue(initial_revenue, saas_sf_growth_rates, num_months)
revenue_saas_us = simulate_revenue(initial_revenue, saas_us_growth_rates, num_months)
revenue_edu_sf = simulate_revenue(initial_revenue, edu_sf_growth_rates, num_months)
revenue_edu_us = simulate_revenue(initial_revenue, edu_us_growth_rates, num_months)
revenue_gen_sf = simulate_revenue(initial_revenue, gen_sf_growth_rates, num_months)
revenue_gen_us = simulate_revenue(initial_revenue, gen_us_growth_rates, num_months)

# Create a DataFrame for better visualization and manipulation
revenue_data = pd.DataFrame({
    'Month': months,
    'SaaS_SF': revenue_saas_sf,
    'SaaS_US': revenue_saas_us,
    'Edu_SF': revenue_edu_sf,
    'Edu_US': revenue_edu_us,
    'Gen_SF': revenue_gen_sf,
    'Gen_US': revenue_gen_us
})

# Plot the revenue data
plt.figure(figsize=(14, 8))

# SaaS
plt.plot(revenue_data['Month'], revenue_data['SaaS_SF'], marker='o', linestyle='-', label='SaaS SF Bay Area')
plt.plot(revenue_data['Month'], revenue_data['SaaS_US'], marker='o', linestyle='-', label='SaaS Nationwide US')

# Education
plt.plot(revenue_data['Month'], revenue_data['Edu_SF'], marker='s', linestyle='--', label='Edu SF Bay Area')
plt.plot(revenue_data['Month'], revenue_data['Edu_US'], marker='s', linestyle='--', label='Edu Nationwide US')

# General
plt.plot(revenue_data['Month'], revenue_data['Gen_SF'], marker='^', linestyle='-.', label='Gen SF Bay Area')
plt.plot(revenue_data['Month'], revenue_data['Gen_US'], marker='^', linestyle='-.', label='Gen Nationwide US')

plt.title('Startup Monthly Revenue Simulation: SF Bay Area vs Nationwide US')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.legend()
plt.show()

# Display the DataFrame
print(revenue_data)
