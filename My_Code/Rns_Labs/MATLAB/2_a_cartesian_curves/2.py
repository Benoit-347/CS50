import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 1000)
y = np.exp(x)
plt.plot(x,y, label = "y = e^x")
plt.title("Grapth of expo")
plt.legend()
plt.grid()
plt.show()