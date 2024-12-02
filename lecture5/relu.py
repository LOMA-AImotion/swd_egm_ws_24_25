# Print relu(x) for x ranging from -10 to 10

def relu(x : int) -> int:
    if x < 0:
        return 0
    else:
        return x

def my_double(x:float) -> float:
    return 2*x
    
if __name__ == "__main__":
    for i in range(-10, 11):
        print(f"x = {i}, relu(x) = {relu(i)}")