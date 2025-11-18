#graph

import numpy, matplotlib
x = numpy.linspace(0, 5, 1000)  #start, stop, number of points
#1 
y = numpy.sin(x)    #makes an array of sin(x) for all values of x

#2
matplotlib.plot(x, y, 'g')   # creates a graph with 1st arg on x axis and 2nd arg on y axis, 3rd arg denotes color
matplotlib.title("Title 1")
matplotlib.legend()     # shows the names of lines in graph by showing what color each one is.
matplotlib.grid()      # shows the grid lines for easy manual navigation
matplotlib.show()   # indicates to code to now project the graph

#1: np.arange(0, 5, 0.001)  # all same, except the 3rd arg shows the space between each point
#2: matplotlib.axes(projection = 'polar')   # indicates the graph to draw in polar format