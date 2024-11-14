def area(width: int, height: int) -> int:
    a = width * height
    print("I'm in the function")
    print(a)
    # here I'm accessing a global variable
    costs_a = cost_per_m2*a
    return a, costs_a

print("I am in the main program")
width_main = int(input("Width?"))
height_main = int(input("Height?"))
cost_per_m2 = 5

my_area, my_costs = area(width_main, height_main)
#print(a) # would not work
print(f"The area is {my_area} at {my_costs} €.")