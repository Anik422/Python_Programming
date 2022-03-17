class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def zero(cls):
        return cls(54, 87)
        
    def draw(self):
        print(f"Point ({self.x} {self.y})")

point1 = Point.zero()
point1.draw()

        

