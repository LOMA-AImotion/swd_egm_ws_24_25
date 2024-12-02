# Store a number of available spots
# Accept requests (name and #spots) from patrons as long as there is still room
# Notify them if you can't offer them spots
# Terminate if all spots are taken
# THIS VERSION IS NOT RECOMMENDED
available_spots = 10
taken_spots = 0

while True:
    # accept requests
    name = input("What's your name?")
    desired_spots = int(input("How many spots would you need?"))
    if desired_spots <= available_spots:
        available_spots -= desired_spots
        print(f"Sure, {name}. We registered your spots. There are still {available_spots} spots available.")
    else: 
        print(f"Sorry {name}, we don't have enough spots.")
    
    # explicit break command if no spots are available
    if available_spots == 0:
        break
