#automating by matching 2 list by looping
import main
a = [[2, 3], [-10,4], [0,0], [2.2,3.3]]
b = [2.5, -3.5, 0.0, 2.75]
for i, j in zip(a, b):
    if main.avge(i) != j:
        print("error:", i[0], "+", i[1], "!=", j)