import um, pytest

def test_1():
    assert um.count("um hello") == 1
def test_1_1():
    assert um.count("um") == 1
def test_2():
    assert um.count("um hello um") == 2
def test_3():
    assert um.count("um um hello") == 2
def test_4():
    assert um.count("um hello um hey um um this is um") == 5
def test_5():
    assert um.count("hello, um, world") == 1
def test_6():
    assert um.count("hello, um, this is um... cs50") == 2
def test_7():
    assert um.count("um? this is um... cs50") == 2
def test_8():
    assert um.count("UM.. this is UM cs50") == 2