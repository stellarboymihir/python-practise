class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point(10, 30)
point1.x = 43
print(point1.x)


