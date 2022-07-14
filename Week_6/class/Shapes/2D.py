from shapes import TwoDimensionalShapes
import math


class Circle(TwoDimensionalShapes):
    def __init__(self, name, radius):
        super().__init__(
            name,
        )
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Square(TwoDimensionalShapes):
    def __init__(self, name, length):
        super().__init__(
            name
        )
        self.number_of_sides = 4
        self.length = length
        assert length >= 1, f"{length} is invalid"

    def perimeter(self):
        return 4 * self.length

    def area(self):
        return 2 * self.length

    def diagonal(self):
        return math.sqrt(self.length * 2)


class Triangle(TwoDimensionalShapes):
    def __init__(self, name, opposite, adjacent, hypothenus):
        super().__init__(
            name
        )
        self.number_of_sides = 3
        self.opposite = opposite
        self.adjacent = adjacent
        self.hypothenus = hypothenus
        assert opposite >= 1, f"opposite is invalid"
        assert adjacent >= 1, f"adjacent is invalid"
        assert hypothenus >= 1, f"hypothenus is invalid"

    def perimeter(self):
        return self.hypothenus + self.adjacent + self.opposite

    def area(self):
        return 0.5 * (self.opposite * self.adjacent)



