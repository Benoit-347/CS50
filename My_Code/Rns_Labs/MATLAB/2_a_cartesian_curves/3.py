import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 1000)
y = 4*x+5
z = 3*x - 1
w = -5*x + 12
plt.plot(x,y, label = "y = 5(x)+2")
plt.plot(x,z, label = "y = -x*x + 1")
plt.plot(x,w, label = "y = x + 2")
plt.title("Grapth of straight lines")
plt.legend()
plt.grid()
plt.show()