import pytest, fuel

#tests

def test_split():
    with pytest.raises(ValueError):
        fuel.convert("2//3")
    with pytest.raises(ValueError):
        fuel.convert("x/y")             #tests the split statement is working

def test_values():
    with pytest.raises(ZeroDivisionError):            #checks for values outside range
        fuel.convert("2/0")
    with pytest.raises(ValueError):
        fuel.convert("2/1")

def test_int():
    assert fuel.convert("1/2") == 50


def test_gauge():
    assert fuel.gauge(50) == "50%"      # testing the guage fn
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
