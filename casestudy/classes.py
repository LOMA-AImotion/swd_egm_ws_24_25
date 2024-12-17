# this is a function
def print_anything(anything):
    print(anything)

class Employee:
    def __init__(self, name, birthdate, qualification):
        self.name = name
        self.birthdate = birthdate
        self.qualification = qualification
        
    # this is a method
    def __str__(self):
        return f"Hello, I am {self.name}. I was born at {self.birthdate} and i have the following qualification: {self.qualification}"
         

class Building:
    def __init__(self, name, walls, windows, roof):
        pass
    
e = Employee("Max Mustermann", "1.1.1999", "M. Sc.")
e2 = Employee("Min Mustermann", "2.1.1999", "B. Sc.")

# print(e.name)
# print(e2.name)

e = str(e)
print(e)