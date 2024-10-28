import main

#how to check for each category? Use multiple functions
def test_pos():
    assert main.avge([2, 3]) == 2.5


def test_negative():
    assert main.avge([-10, 3]) == -3.5
    

def test_0():
    assert main.avge([0, 0]) == 0


def test_fraction():
    assert main.avge([2.3, 3.2]) == 2.75
    
#notice that works fn call not given, checks delclarations until 1 error in each delclarations (not nested def)
#Note: checks declations only when fn call not given