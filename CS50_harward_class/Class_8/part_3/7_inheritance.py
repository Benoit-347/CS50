class Role:
    var_class = 10
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        else:
            self.name = name

class Student(Role):    # passing Role as parameter only gives this class access, need further statements to cpy attributes
    def __init__(self, name, house):
        super().__init__(name)      # Call the parent __init__ method, which by our code, initializes the arg passed to attribute 'name'
        self.house = house              # we use this method, so tht the child's __init__ does not overwrite the __init__ of parent.

    # why use the parent init under the child init?
    # -The init has to be initialized by the child, as super()__init__ will not call the parent directly. Hence child has to call init first, then hands it over to parent. 

class Professor(Role):   
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

obj = Student("Benoit", "Red")
obj_2 = Professor("Vincent", "CSE")
print(obj.name)
print(f"Mr. {obj_2.name} teaches {obj_2.subject}")
print(Professor.var_class)  # obtains access, to access variables at parent class