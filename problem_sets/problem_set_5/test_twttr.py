import twttr, pytest

def main():
     test_capital()
     test_small()
     test_numbers()
     test_punctuation()

# all tests
def test_capital():         #test uppercase
    word1 = "HELLO ALL YOU INVESTORS"
    assert twttr.shorten(word1) == "HLL LL Y NVSTRS"

def test_small():           #test lowercase
    word1 = "hello all you investors"
    assert twttr.shorten(word1) == "hll ll y nvstrs"

def test_numbers():         #test numbers
    word1 = "hello 123"
    assert twttr.shorten(word1) == "hll 123"

def test_punctuation():     #test punctuations
    word1 = "hello world@!#"
    assert twttr.shorten(word1) == "hll wrld@!#"




if __name__ == "__main__":
    main()
