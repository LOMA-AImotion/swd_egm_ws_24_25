def volume(width: int, height : int, depth:int, costs:int = 1, tax:float = 1.19 ) -> int:
    return width * height * depth * costs * tax

#print(volume(height=10, width=20, depth=5, costs=2))
print(volume(10, 20, 5, costs=2, tax=1.07))
# **kwargs for unlimited arguments