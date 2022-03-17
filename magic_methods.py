class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x} {self.y})"


point = Point(1, 2)
print(str(point))
print(type(point))
print(point)

        