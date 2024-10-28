#How do you check if program code works as intended? You manually input each value. Automate? Create a fn
import main
def test():  
    if main.avge([2, 3]) != 2.5:
        print("avge(2, 3 not 2.5)")
    if main.avge([-10, 3]) != -3.5:
        print("avge(-10, 3 not -3.5)")
    if main.avge([0, 0]) != 0:
        print("avge(0, 0 not 0)")
    if main.avge([2.3, 3.2]) != 2.75:
        print("avge(2.3, 3.2 not 2.75)")

    if main.avg([2, 3]) != 2.5:
        print("avge(2, 3 not 2.5)")
    if main.avg([-10, 3]) != -3.5:
        print("avge(2, 3 not 2.5)")
    if main.avg([0, 0]) != 0:
        print("avge(2, 3 not 2.5)")
    if main.avg([2.3, 3.2]) != 2.75:
        print("avge(2, 3 not 2.5)")
test()