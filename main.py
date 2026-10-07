from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def move(self, other):
        self.x += other.x
        self.y += other.y

p1 = Point(0, 0)

x_move = float(input("x: "))
y_move = float(input("y: "))

p1.move(Point(x_move, y_move))
print(p1.x, p1.y)

