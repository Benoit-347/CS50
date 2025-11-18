import matplotlib.pyplot as plt
fig = plt.figure()
main_ax = plt.axes([0.1, 0.1, 0.8, 0.8])  # Main plot
inset_ax = plt.axes([0.6, 0.6, 0.2, 0.2])  # Inset plot
main_ax.plot([0, 1], [0, 1])
inset_ax.plot([0, 1], [1, 0])
plt.show()
