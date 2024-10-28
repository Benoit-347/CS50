#getting clues when getting error
import main
def test():
    try:
        assert main.avge([2, 3]) == 2.5
    except:
        print("[2, 3]) != 2.5")
    try:
        assert main.avge([-10, 3]) == -3.5
    except:
        print("[-10, 3]) != -3.5")
    try:
        assert main.avge([0, 0]) == 0
    except:
        print("[0, 0]) != 0")
    try:
        assert main.avge([2.3, 3.2]) == 2.75
    except AssertionError:
        print("[2.3, 3.2]) != 2.75")


test()