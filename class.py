#class : blueprint for creating new objects
#objects : instance of a class

#class : human
#objects : john, mary, jack, anik
from email.policy import default


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.z = z

        
    default_color = "Rad"


    def draw(self):
        print(f"Point ({self.x}, {self.y}, {self.z})")

a, b= map(int ,input("Enter two number :").split())
Point.z = 10
point1 = Point(a,b)
print(point1.default_color)
print(Point.default_color)
point1.draw()

a, b= map(int ,input("Enter tow number :").split())
Point.z = 20
point2 = Point(a,b)
print(point2.default_color)
print(Point.default_color)
point2.draw()
# print(type(point))
# print(isinstance(point, Point)) #point ki Point class ar object aita check kore