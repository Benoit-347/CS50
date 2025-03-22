import pytest, sys
import bank

def main():     # catching errors
    try:
        test_h()
        test_hello()
        test_no_similar()
    except:
        pass

# checking the greeting hello
def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("HELLO BRO") == 0

# checking the greeting satrign with h
def test_h():
    assert bank.value("hey") == 20
    assert bank.value("HEY") == 20
    assert bank.value("HEY BRO") == 20

# checking the greeting other than starting with h
def test_no_similar():
    assert bank.value("nice") == 100
    assert bank.value("NICE") == 100
    assert bank.value("Nice Bro") == 100


main()
