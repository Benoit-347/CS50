import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 4, 1000)
a = 5
y = (x**2*((a+x)/(a-x)))**0.5
z = (x**2*((a+x)/(a-x)))**0.5*-1
plt.plot(x,y)
plt.plot(x,z)
plt.title("Grapth of strophoid")
plt.legend()
plt.grid()
plt.show()