import numpy as np
import matplotlib.pyplot as plt

# Data points
n = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
f_n = np.array([262, 608, 936, 1324, 1650, 2039, 2453, 2894, 3426, 3716])
g_n = np.array([259, 605, 933, 1315, 1645, 2038, 2446, 2893, 3421, 3715])

# Plotting the actual data points for f(n) and g(n)
plt.scatter(n, f_n, color='blue', label='f(n)', s=80)
plt.scatter(n, g_n, color='orange', label='g(n)', s=80)

# Plotting the trend lines for f(n) and g(n)
plt.plot(n, f_n, color='blue', linestyle='-',linewidth=1)
plt.plot(n, g_n, color='orange', linestyle='-',linewidth=1)

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Function values')
plt.title('Comparison of f(n) and g(n)')
#plt.ylim(min(min(f_n), min(g_n)) - 100, max(max(f_n), max(g_n)) + 100)

# Adding a legend
plt.legend()

# Display the plot
plt.show()
