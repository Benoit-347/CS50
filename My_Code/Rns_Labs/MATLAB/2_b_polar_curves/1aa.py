import numpy as np
import matplotlib.pyplot as plt

# Set up the polar plot
plt.figure()
ax = plt.subplot(111, projection='polar')

# Parameters
a1 = 5
theta = np.arange(0, 2 * np.pi, 0.001)

# Calculate radii for the cardioid
r_inner = a1 * (1 - np.cos(theta))
r_outer = a1 * (1 + np.cos(theta))

# Plotting the cardioid
ax.plot(theta, r_inner, color='g', label='Inner Cardioid')
ax.plot(theta, r_outer, color='y', label='Outer Cardioid')

# Adding title and legend
plt.title('Graph of Cardioid')
plt.legend()
plt.show()