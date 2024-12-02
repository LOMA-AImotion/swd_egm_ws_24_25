# Ask for a fixed budget (an int)
# "Buy" square numbers as long as there is still some budget left
# Print the largest square's side length and the overall sum you spent

budget = int(input("What's my budget?"))
sum_squares = 0
square_length = 1
squares = []

while sum(squares) <= budget : # there is budget 
    square = square_length * square_length
    squares.append(square)
    #budget = budget - square
    #sum_squares = sum_squares + square
    square_length += 1 
    #print(f"Square {square}")

# eliminating the last one due to overshoot:
squares.pop()
print(squares)
print(f"The largest number I could buy was {len(squares)}, I totaled at {sum(squares)}.")