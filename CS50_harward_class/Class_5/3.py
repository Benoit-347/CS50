#how to get error output when test condition fails? 
#assert
import main
def test():
    assert main.avge([2, 3]) == 2.5

    assert main.avge([-10, 3]) == -3.5

    assert main.avge([0, 0]) == 0

    assert main.avge([2.3, 3.2]) == 2.75

    assert main.avg([2, 3]) == 2.5

    assert main.avg([-10, 3]) == -3.5

    assert main.avg([0, 0]) == 0

    assert main.avg([2.3, 3.2]) == 2.75
test()