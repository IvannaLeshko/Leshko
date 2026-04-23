class Quadrilateral:
    def area(self):
        return 0

    def __str__(self):
        return f"Площа: {self.area()}"


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Parallelogram(Quadrilateral):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h


class Trapezoid(Quadrilateral):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) / 2 * self.h


for shape in [Rectangle(4, 5), Parallelogram(6, 3), Trapezoid(4, 6, 5)]:
    print(type(shape).__name__, "->", shape.area())