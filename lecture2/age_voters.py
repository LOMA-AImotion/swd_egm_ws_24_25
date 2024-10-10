# Read user name and age
# Define legal voting age
# Report to the user for how many years they have been allowed to vote

name = input("What's your name?")
age = input("How old are you?")
age = int(age)

legal_voting_age = 16
years_allowed_to_vote = age - legal_voting_age

# print("Hi ", name, "You have been allowed to vote for ", years_allowed_to_vote, " years.")
print(f"Hi {name}, you have been allowed to vote for {years_allowed_to_vote} years.")