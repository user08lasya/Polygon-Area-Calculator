from abc import ABC, abstractmethod


class Polygon(ABC):
   def area(self):
        pass


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


triangle = Triangle(5, 10)
rectangle = Rectangle(4, 6)
circle = Circle(5)

print(f"Area of Triangle: {triangle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
print(f"Area of Circle: {circle.area()}")

