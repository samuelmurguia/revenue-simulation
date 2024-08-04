import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the simulation
num_months = 24
initial_revenue = 15000  # Initial monthly revenue

# Best-case scenario parameters
best_very_high_growth_rate = 0.30  # 30% monthly growth for the first 6 months
best_moderate_growth_rate = 0.20  # 20% monthly growth for the next 12 months
best_stabilized_growth_rate = 0.10  # 10% monthly growth for the remaining period

# Worst-case scenario parameters
worst_high_growth_rate = 0.05  # 5% monthly growth for the first 6 months
worst_slow_growth_rate = 0.03  # 3% monthly growth for the next 12 months
worst_minimal_growth_rate = 0.01  # 1% monthly growth for the remaining period

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

# Simulate revenue for best-case and worst-case scenarios
months = np.arange(1, num_months + 1)
revenue_best = simulate_revenue(initial_revenue, [best_very_high_growth_rate, best_moderate_growth_rate, best_stabilized_growth_rate], num_months)
revenue_worst = simulate_revenue(initial_revenue, [worst_high_growth_rate, worst_slow_growth_rate, worst_minimal_growth_rate], num_months)

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
plt.title('Online Education Startup Monthly Revenue Simulation: Best vs Worst Case')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.legend()
plt.show()

# Display the DataFrame
print(revenue_data)
