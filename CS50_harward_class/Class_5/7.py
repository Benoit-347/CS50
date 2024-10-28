#check for str and default value
from main import hello
def test():
    def argument():
        assert hello("ben") == "hello ben"
    def default():
        assert hello() == "hello world"
    argument()
    default()
test()

def test2():
    a = ["ben", "dhanush", "deekshith"]
    for i in a:
        assert hello(i) == f"hello {i}"
test2()
#__inint__.py file makes its folder a package folder