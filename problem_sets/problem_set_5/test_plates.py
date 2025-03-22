import pytest
import plates

def main():
    try:
        test_length()
        test_first_2_letters()
        test_number()
        test_special_char()
        test_true_pattern()
    except:
        pass

# test cases
def test_length():
    assert plates.is_valid("ab12345") == False
    assert plates.is_valid("a") == False

def test_first_2_letters():
    assert plates.is_valid("34612") == False

def test_number():
    assert plates.is_valid("34ab45") == False
    assert plates.is_valid("aa2abc") == False
    assert plates.is_valid("aa0345") == False

def test_special_char():
    assert plates.is_valid("ab 123") == False
    assert plates.is_valid("ab *12") == False

def test_true_pattern():
    assert plates.is_valid("ab1234") == True
    assert plates.is_valid("abcdef") == True
    assert plates.is_valid("ABCCDE") == True
    assert plates.is_valid("ABCC34") == True

