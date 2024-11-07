friends = ["Rick", "Carl", "Maggie"]
#answers = ["Yes", "No", "Not sure", "Maybe"]
answers = ["Yes", "No", "Not sure"]

if len(friends) != len(answers):
    raise ValueError(f"Lengths of input lists don't match: {friends}, {answers}")
else:
    print(list(zip(friends, answers)))