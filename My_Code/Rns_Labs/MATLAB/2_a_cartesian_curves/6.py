import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4, 4, 1000)
r = 5
y = (4*x)**0.5
z = (4*x)**0.5*-1
plt.plot(x,y)
plt.plot(x,z)
plt.title("Graph of Parabola")
plt.legend()
plt.grid()
plt.show()