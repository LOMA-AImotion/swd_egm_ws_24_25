# Checks whether a user is taller than 150 cm and grant access if so

height = int(input("How tall are you?"))
if height > 150:
    print("Congrats") 
    print("You may ride")
else: 
    print("No chance, you're too small") 