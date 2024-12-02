radio_button = ["Radio Button", 234]
window_button = ["Window Button", 678]
seat_height_button = ["Seat height button", 258]
seat_belt_in_meter = ["Seat belt in meter", 63.7]
main_driver_screen = ["Main driver screen", 90]
steering_wheel_button = ["Steering wheel button", 941]

inventory = [radio_button, window_button, seat_height_button, seat_belt_in_meter, main_driver_screen, steering_wheel_button]

part_index = 0
for part in inventory:
    print(f"part name: {part[0]} -> {part_index}; ({part[1]} available)")
    part_index += 1
    # equivalent: 
    # part_index = part_index + 1

order = int(input("Which product do you want to order? "))
quantity = float(input("How much of the product do you want to order? "))

shopping_cart = None

ordered_product = inventory[order]
available_quanity = ordered_product[1]

if available_quanity >= quantity:
    inventory[order][1] -= quantity
    shopping_cart = quantity
else:
    print("Sorry, your order cannot be fulfilled!")

        
print(f"Your order consists of the following stuff: {shopping_cart}")

    
