from functools import partial

def my_add(x: int, y: int) -> int:
    return x + y

g = partial(my_add, 5)
h = partial(g, 20)

print(my_add(5, 7))
print(g(10))
print(h())