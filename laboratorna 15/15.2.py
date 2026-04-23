import math

class FlatFigure:
    def area(self):
        return 0

    def __str__(self):
        return f"{type(self).__name__} -> площа: {self.area()}"


class Circle(FlatFigure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(math.pi * self.r ** 2, 2)


class Sphere(FlatFigure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(4 * math.pi * self.r ** 2, 2)


class Ellipse(FlatFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return round(math.pi * self.a * self.b, 2)


for shape in [Circle(5), Sphere(5), Ellipse(4, 3)]:
    print(shape)