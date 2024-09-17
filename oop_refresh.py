class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other) -> float:
        return Vector(self.x + other.x, + self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"


v1 = Vector(10,30)
v2 = Vector(20,10)
v3 = v1+v2

print(v3)