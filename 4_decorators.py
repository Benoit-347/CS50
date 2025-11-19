# decorators: fns to get and set atributes (but this can also done using the '.' operator)

class Student:
    
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    # Getter    Terminology in java
    @property
    def house(self):
        return self._house   # cannot have instance_variables same name as fn_name (house), we can show the itepretor that we are refering to the instance variable instead of fn itself, using a '_' prefix to var name, 
    
    # Setter            and to allow only certain values that can be assigned to attribute house:
    @house.setter   # this below fn, will now be called each time a attribute with this fn name is assigned (1. at __init__ construcotr, 2. at manual member assignemtn 3. if using mehtods to assign members)
    def house(self, house):
        if house not in ["red", "green", "yellow", "blue"]:
            raise ValueError
        self._house = house
    

def main():
    obj = Student("Benoit", "green")
    print(obj)
    obj.house = 'a'     # this assignment to attribute, matches all methods in class with same attribute anem, using self asa first arg and calls them.

main()