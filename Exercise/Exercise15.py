class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

Circle_area = Circle(3)
print(Circle_area.area())