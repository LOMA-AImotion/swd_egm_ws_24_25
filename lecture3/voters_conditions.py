# Ask a voter for their age
# Compare to the legal voting age
# - if younger - show how many years to wait
# - if exactly that age - congrats on first voter
# - otherwise how many years have you been allowed to vote 
# ==========================================================
name = input("What's your name?")
age = int(input("How old are you?"))

voting_age = 18
if age < voting_age:
    print(f"Sorry, you're only {age}. You have to wait for {voting_age - age} more years.")
elif age == voting_age:
    print(f"Congrats, {name}, you're a first-time voter!")
else: # age > voting_age 
    print(f"{name}, you have been allowed to vote for {age - voting_age} years.")
#elif age > voting_age: 