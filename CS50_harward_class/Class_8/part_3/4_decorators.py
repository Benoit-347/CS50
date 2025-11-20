# decorators: they are fns tht apply settings to other fns. (use case- while returning (get) and assigning (set) attributes which was usually done by the '.' operator

class Student:
    
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    # Getter    Terminology in java; redirects attribute return - returns this value when accessing attribute of the def. fn name
    @property       # when doing obj.house => the return of getter is returned intead, while accessing
    def house(self):
        return self._house   # using a '_' prefix to var name, to acess actual instance attribute, bypassing getter (and setter )
    
    # to allow only certain values that can be assigned to attribute house:
    # Setter
    @house.setter   # this below fn, will now be called, in place of a attribute assignment, fn has same name as attribute 
    def house(self, house):     # (called automatically at- 1. at __init__ construcotr, 2. at manual member assignment, 3. even inside a method to assign this specific member)
        if house not in ["red", "green", "yellow", "blue"]:     # has 2 args as 1st is obj, to load to mem; 2nd is the attribute itself 
            raise ValueError("Invalid house")
        self._house = house
    # NOTE: Python does NOT assign obj.house ever, the setter function is called instead
        # Python itself never directly assigns obj.house when a property exists
            # Python internally turns the attribute house into a descriptor object with a __set__ method.

def main():
    obj = Student("Benoit", "green")
    print(obj)
    obj.house = 'red'     # this assignment to attribute, matches all methods in class with same attribute anem, using self asa first arg and calls them.


main()

# NOTE: all of the methods here are instance methods. And all of the attributes here are also instance attributes. i.e. a obj of the class has to be created before a fn can be used on them. Like str.copy() vs a = str("hello"), a.copy() the former is a class method and latter, an instance method.