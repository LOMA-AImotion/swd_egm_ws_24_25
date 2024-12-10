# # Tuples 
# radio_button_tuple = ("Radio Button", 234)
# # This will trigger an error:
# # radio_button_tuple[0] = "RadioButton"

# # Sets
# item_set = {"item1", "item2", "item3", "item1"}
# print(f"Set: {item_set}")
# if "item10" in item_set:
#     print("In set")
# else:
#     print("not in set")

# # Dictionaries
# item_dict = {"item1": 12, "item2": 23, "item3": 34}
# print(item_dict["item2"])

# # Functions
# def calculate_product(x1, x2, percentage=0.9, bias=1.0):
#     """
#     Calculates stuff. 
    
#     Args:
#         x1: first parameter
#         x2: second parameter
#         percentage: scaling value
#         bias: bias value
    
#     Returns:
#         Result of the calculation as int 
#     """
#     result = x1 * x2
#     return (percentage * result) + bias

# def calculate_product(x1, x2, percentage=0.9, bias=1.0):
#     result = x1 * x2
#     return (percentage * result) + bias


# result = calculate_product(2, 3, bias=2.0, percentage=0.8)
# print(f"result: {result}")

def display_inventory(inventory):
    print("Hello dear customer, this is our inventory:")
    print(20*"-") 

    for name, product_inventory in inventory.items():
        amount = product_inventory[0]
        unit = product_inventory[1]
        print(f"{name}: {amount} {unit}")
    print(20*"-") 

# TODO add categories that the user can select first  
inventory = {"Radio Button": [234, "pieces"], "Window Button": [678, "pieces"], "Seat height button": [258, "pieces"], "Seat belt": [63.7, "meter"]}

display_inventory(inventory)

order = input("Which product do you want to order? ")
quantity = float(input("How much of the product do you want to order? "))

shopping_cart = None

ordered_product = inventory[order]
available_quanity = ordered_product[0]

if available_quanity >= quantity:
    inventory[order][0] -= quantity
    shopping_cart = quantity
else:
    print("Sorry, your order cannot be fulfilled!")

        
print(f"Your order consists of the following stuff: {shopping_cart}")
print(f"Our inventory after your order: {inventory}")

# TODO add functions
# TODO allow for multiple products in shopping cart 
# TODO give possibility to edit shopping cart before payment
# TODO customer needs to enter personal information for invoice  
