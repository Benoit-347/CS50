class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"name: {self.name}, house: {self.house}"
    
    def get_attributes(self):
        return (self.name, self.house)
    def get_first_alphabet(self):
        return self.name[0]
    
def main():
    obj = Student("Benoit", "Red")
    print(obj.get_attributes()) # here the fn copies the ref of the obj that calls it, as its first arg 
    print(obj.get_first_alphabet()) # runs a slicing within its obj, to its attribute name. and returns the string/

main()