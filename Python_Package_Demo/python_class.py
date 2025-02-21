class Point:

    # Contructor Initialization. Self is current object.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Moved")

    def draw(self):
        print("Drawn")


point1 = Point(10, 20)
point1.draw()
point1.move()

print(f'Point: ({point1.x}, {point1.y})')
