radion_button = 234
window_button = 678
seat_height_button = 258
seat_belt_in_meter = 63.7
main_driver_screen = 90
steering_wheel_button = 941


print("radion_button: 1")
print("window_button: 2")
print("seat_height_button: 3")
print("seat_belt_in_meter: 4")
print("main_driver_screen: 5")
print("steering_wheel_button: 6")

order = input("Which product do you want to order? ")
quantity = float(input("How much of the product do you want to order? "))

shopping_cart = None

if order == "1":
    if radion_button >= quantity:
        radion_button = radion_button - quantity
        shopping_cart = quantity
if order == "2":
    if window_button >= quantity:
        window_button = window_button - quantity
        shopping_cart = quantity
if order == "3":
    if seat_height_button >= quantity: 
        seat_height_button = seat_height_button - quantity
        shopping_cart = quantity
        
# ... and so on, for the other options it's the same
        
print(f"Your order consists of the following stuff: {shopping_cart}")

    
