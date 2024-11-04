#linking (or shared references) happens with all mutable data types in Python
#When you assign one mutable object to another variable, both variables point to the same object in memory
#int, str, tuple are not susceptible to this 
def main1():
    a = [2, 3]
    b = a
    def c():
        a[0] = 4
    c()
    print(b)