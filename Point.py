class Point:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


p1 = Point(10, 10)
p2 = Point(10, 10)

if p1 == p2:
    print("=")
else:
    print("!")

p1.x = 1
if p1 != p2:
    print("!")
else:
    print("=")
