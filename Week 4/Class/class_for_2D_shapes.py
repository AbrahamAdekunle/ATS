from math import pi


class Circle:
    # pi = 3.142
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return f" area of a circle is {(pi * (self.radius ** 2))}"

    def get_perimeter(self):
        return f"the perimeter of a circle is {(2 * pi * self.radius)}"


class Parallelogram:
    def __init__(self, base, height, a, b, c):
        self.base = base
        self.height = height
        self.length_of_a = a
        self.length_of_b = b
        self.length_of_c = c

    def get_area(self):
        return f"the area of a parallelogram is {(self.base * self.height)} "

    def get_perimeter(self):
        return f"the perimeter is {(2 * (self.length_of_a + self.length_of_b))}"


class Trapezoid:
    def __init__(self, height, a, b, c, d):
        self.height = height
        self.length_of_a = a
        self.length_of_b = b
        self.length_of_c = c
        self.length_of_d = d

    def get_area(self):
        return f"the area is {(0.5 * (self.length_of_a + self.length_of_b) * self.height)}"

    def get_perimeter(self):
        return f"the perimeter is {sum((self.length_of_c, self.length_of_d, self.length_of_b, self.length_of_a))} "


class Triangle:
    def __init__(self, a, b, c):
        self.length_of_a = a
        self.length_of_b = b
        self.length_of_c = c

    def get_area_perimeter(self, base, height):
        return f"the area is{(0.5 * base * height)}"

    def get_perimeter(self):
        return f"the perimeter is {(self.length_of_a + self.length_of_b + self.length_of_c)} "


# trap = Trapezoid(3, 4, 5, 6, 7)
# print(trap.get_area())


c = Circle(24)
print(c.get_area())
