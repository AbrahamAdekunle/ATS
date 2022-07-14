import math

from shapes import ThreeDimensionalShapes


class Cube(ThreeDimensionalShapes):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length
        assert length >= 1, f"length is invalid"

    def volume(self):
        return self.length ** 3

    def surface_area(self):
        return 6 * (self.length ** 2)

    def space_diagonal(self):
        return math.sqrt(3 * self.length)


class Sphere(ThreeDimensionalShapes):
    def __init__(self, name, radius):
        super().__init__(
            name
        )

        self.radius = radius
        assert radius >= 1, f"radius is invalid"

    def volume(self):
        return (4 / 3) * 3.14 * (self.radius ** 3)

    def surface_area(self):
        return 4 * 3.14 * (self.radius ** 2)


class Tetrahedron(ThreeDimensionalShapes):
    def __init__(self, name, length):
        super().__init__(
            name
        )
        self.length = length
        assert length >= 1, f"length is invalid"

    def volume(self):
        return (self.length ** 3) / (6 * math.sqrt(2))

    def height(self):
        return math.sqrt((2 / 3) * self.length)

    def surface_area(self):
        return math.sqrt(3 * (self.length ** 2))

    def face_area(self):
        return (math.sqrt(3) / 4) * (self.length ** 2)
