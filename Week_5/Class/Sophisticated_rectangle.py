class SophisticatedRectangle:

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        assert x1 <= 20.0, f"x1 {x1} is greater than 20.0"
        assert y1 <= 20.0, f"y1 {y1} is greater than 20.0"
        assert x2 <= 20.0, f"x1 {x2} is greater than 20.0"
        assert y2 <= 20.0, f"x1 {y2} is greater than 20.0"
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.set_func(x1, y1, x2, y2)

    def set_func(self, x1, y1, x2, y2):
        self.co_ordinate = {(x1, y1), (x2, y2)}

    def __str__(self):
        return f"{self.co_ordinate}"

    def length(self):
        if self.x1 > self.x2:
            return self.x1 - self.x2
        elif self.x2 > self.x1:
            return self.x2 - self.x1

    def width(self):
        if self.y1 > self.y2:
            return self.y1 - self.y2
        elif self.y2 > self.y1:
            return self.y2 - self.y1

    def perimeter(self):
        return 2 * (self.length() + self.width())

    def area(self):
        return self.width() * self.length()

    def issquare(self):
        if self.width() == self.length():
            return f"This is a Square"


rect = SophisticatedRectangle(2, 2, 2, 2)
print(rect.issquare())
