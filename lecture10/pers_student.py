class Person:
    def __init__(self, name:str ):
        self.name = name

    def greet(self):
        print(f"Hi, I am", self.name)

class Student(Person):
    def __init__(self, name, mat_id):
        super().__init__(name)
        self.__mat_id = mat_id
    
    def greet(self):
        print(f"Hi I am {self.name}, I study EGM and my mat id is {self.__mat_id}.")

if __name__ == "__main__":
    s = Student("Faruk", 1234)
    s.greet()

    p = Person("Caroline")
    p.greet()
