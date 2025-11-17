import numb3rs

def test_1():
    assert numb3rs.validate("255.300.1.4") == False
def test_2():
    assert numb3rs.validate("255.1.300.4") == False
    assert numb3rs.validate("255.1.2.300") == False
    assert numb3rs.validate("300.1.2.4") == False
def test_3():
    assert numb3rs.validate("255.1.200.4.5") == False
