import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the simulation
num_months = 24
initial_revenue = 15000  # Initial monthly revenue

# Best-case scenario parameters
very_high_growth_rate = 0.25  # 25% monthly growth for the first 6 months
moderate_growth_rate = 0.15  # 15% monthly growth for the next 12 months
stabilized_growth_rate = 0.08  # 8% monthly growth for the remaining period

# Worst-case scenario parameters
high_growth_rate = 0.08  # 8% monthly growth for the first 6 months
slow_growth_rate = 0.04  # 4% monthly growth for the next 12 months
minimal_growth_rate = 0.01  # 1% monthly growth for the remaining period

# Generate the revenue data for best-case scenario
months = np.arange(1, num_months + 1)
revenue_best = np.zeros(num_months)

for month in range(num_months):
    if month == 0:
        revenue_best[month] = initial_revenue
    elif month < 6:
        revenue_best[month] = revenue_best[month - 1] * (1 + very_high_growth_rate)
    elif month < 18:
        revenue_best[month] = revenue_best[month - 1] * (1 + moderate_growth_rate)
    else:
        revenue_best[month] = revenue_best[month - 1] * (1 + stabilized_growth_rate)

# Generate the revenue data for worst-case scenario
revenue_worst = np.zeros(num_months)

for month in range(num_months):
    if month == 0:
        revenue_worst[month] = initial_revenue
    elif month < 6:
        revenue_worst[month] = revenue_worst[month - 1] * (1 + high_growth_rate)
    elif month < 18:
        revenue_worst[month] = revenue_worst[month - 1] * (1 + slow_growth_rate)
    else:
        revenue_worst[month] = revenue_worst[month - 1] * (1 + minimal_growth_rate)

# Create a DataFrame for better visualization and manipulation
revenue_data = pd.DataFrame({
    'Month': months,
    'Best_Case_Revenue': revenue_best,
    'Worst_Case_Revenue': revenue_worst
})

# Plot the revenue data
plt.figure(figsize=(10, 6))
plt.plot(revenue_data['Month'], revenue_data['Best_Case_Revenue'], marker='o', linestyle='-', color='g', label='Best Case')
plt.plot(revenue_data['Month'], revenue_data['Worst_Case_Revenue'], marker='o', linestyle='-', color='r', label='Worst Case')
plt.title('Online Education Startup Monthly Revenue Simulation')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.legend()
plt.show()

# Display the DataFrame
print(revenue_data)
