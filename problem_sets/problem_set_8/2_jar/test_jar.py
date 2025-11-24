import pytest
import jar

def test_init():
    obj_jar = jar.Jar(10)
    assert bool(obj_jar) == True

obj_jar = jar.Jar(10)
def test_deposit():
    obj_jar.deposit(5)
    assert obj_jar.n == 5

def test_withdraw():
    obj_jar.withdraw(3)
    assert obj_jar.n == 2

def test_str():
    assert str(obj_jar) == '🍪🍪'
