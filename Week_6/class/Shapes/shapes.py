import math


class Shapes:

    def __init__(self, name: str):
        self.name = name


class TwoDimensionalShapes(Shapes):
    def __init__(self, name):
        super().__init__(
            name
        )


class ThreeDimensionalShapes(Shapes):
    def __init__(self, name):
        super().__init__(
            name
        )
