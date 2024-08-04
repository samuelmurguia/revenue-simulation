import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
initial_users = 10000
carrying_capacity = 1000000
time_period = 24

# Monthly growth rates to reflect more realistic adoption patterns
monthly_growth_rates = [
    0.25, 0.25, 0.20, 0.20, 0.15, 0.15,  # Initial high growth due to marketing
    0.10, 0.10, 0.08, 0.08, 0.06, 0.06,  # Steady growth
    0.12, 0.12, 0.10, 0.10, 0.08, 0.08,  # Back-to-school season boost
    0.05, 0.05, 0.04, 0.04, 0.03, 0.03   # Slowing down as saturation approaches
]

# Logistic growth function with variable growth rates
def logistic_growth_variable(P0, K, rates, months):
    population = np.zeros(len(months))
    population[0] = P0
    for i in range(1, len(months)):
        r = rates[i-1]
        P = population[i-1]
        population[i] = P + r * P * (1 - P / K)
    return population

# Generate the time points
time_points = np.arange(0, time_period + 1)

# Calculate the number of users for each time point
users = logistic_growth_variable(initial_users, carrying_capacity, monthly_growth_rates, time_points)

# Create a DataFrame for better visualization
growth_data = pd.DataFrame({
    'Month': time_points,
    'Users': users
})

# Plot the logistic growth with variable rates
plt.figure(figsize=(10, 6))
plt.plot(growth_data['Month'], growth_data['Users'], marker='o', linestyle='-', color='b')
plt.title('Natural Growth Simulation of Online Education with Variable Monthly Rates')
plt.xlabel('Month')
plt.ylabel('Number of Users')
plt.grid(True)
plt.show()

# Display the DataFrame
print(growth_data)
