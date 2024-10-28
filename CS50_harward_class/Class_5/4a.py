#using more organized output to find error? run with pytest
#had to install pytest and add path to system variable: C:\Users\benoi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts
#assert
import main

assert main.avge([2, 3]) == 2.5

assert main.avge([-10, 3]) == -3.5

assert main.avge([0, 0]) == 0

assert main.avge([2.3, 3.2]) == 2.75

assert main.avg([2, 3]) == 2.5

assert main.avg([-10, 3]) == -3.5

assert main.avg([0, 0]) == 0

assert main.avg([2.3, 3.2]) == 2.75
test()

#note that pytest is written to check first error and show its comparison for main code
