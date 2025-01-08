class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"Servus, my name is {self.first_name} {self.last_name}")

if __name__ == "__main__":
    p = Person("Jane", "Doe")
    p.last_name = "Doenahue"
    p.greet()