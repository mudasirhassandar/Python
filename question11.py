class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        self.area = 3.14 * (self.radius * self.radius)
        print("Area =", self.area)

    def get_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        print("Perimeter =", self.perimeter)


circle1 = Circle(3)
circle1.get_area()
circle1.get_perimeter()
