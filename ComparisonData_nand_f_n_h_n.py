import numpy as np
import matplotlib.pyplot as plt

# Data points
n = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
f_n = np.array([250, 584, 957, 1302, 1710, 2127, 2419, 2869, 3294, 3693])

# Quadratic function h(n) = -99.25 + 3.387n + 0.000408n^2
h_n = -99.25 + 3.387 * n + 0.000408 * n**2

# Plotting the actual data points
plt.scatter(n, f_n, color='blue', label='Actual f(n)')  # Label for actual data points

# Plotting the quadratic model
plt.plot(n, h_n, color='red', label='Model h(n)')  # Label for the model

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Function values')
plt.title('Comparison of f(n) and h(n)')

# Adding a legend
plt.legend()  # This command adds a legend to the plot

# Display the plot
plt.show()
