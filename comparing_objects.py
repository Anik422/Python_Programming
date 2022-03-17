import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # def __str__(self):
    #     return f"Point({self.x} {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return self.x != other.x and self.y != other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
        
point1 = Point(21, 51)
point2 = Point(22, 52)
print(point1 + point2)
