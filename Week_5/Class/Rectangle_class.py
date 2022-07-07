class Rectangle:
    def __init__(self, length=1.0, width=1.0) -> None:
        self.length = length
        self.width = width

    def __str__(self):
        return f" Rectangle (length = {self.__length}, width = {self.__width})"

    def get_length(self):
        return self.__length

    def set_length(self, length: float):
        if length < 0.0 or length > 20.0:
            raise ValueError("Error! length higher than 20.0 or lower than.0.0 ")
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width: float):
        if width < 0.0 or width > 20.0:
            raise ValueError("Error! width higher than 20.0 or lower than.0.0 ")
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    width = property(fget=get_width, fset=set_width)
    length = property(fget=get_length, fset=set_length)


shape = Rectangle(0.9, 2.0)
print(shape)

