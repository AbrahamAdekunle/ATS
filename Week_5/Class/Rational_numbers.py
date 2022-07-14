class RationalNumber:
    def __init__(self, numerator: 1.0, denominator: 2.0):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self, denominator: float):
        if denominator < 1:
            raise ValueError("input is not valid")
        self.__denominator = denominator

    denominator = property(fset=set_denominator, fget=get_denominator)

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            raise Exception("Invalid data type")
        else:
            if self.denominator == other.denominator:
                return RationalNumber.reduced_form((self.numerator + self.numerator), self.denominator)
            else:
                if self.denominator % other.denominator == 0:
                    denom = self.denominator / other.denominator
                    RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) + (other.numerator * self.denominator)), denom)
                elif other.denominator % self.denominator == 0:
                    denom = other.denominator / self.denominator
                    RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) + (other.numerator * self.denominator)), denom)
                else:
                    denom = self.denominator * other.denominator
                    return RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) + (other.numerator * self.denominator)), denom)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            raise ValueError("Invalid data type")
        return RationalNumber.reduced_form((self.numerator * other.numerator), (self.denominator * other.denominator))

    def __truediv__(self, other):
        if not isinstance(other, RationalNumber):
            raise Exception("Invalid data type")
        return RationalNumber.reduced_form((self.numerator * other.denominator), (other.numerator * self.denominator))

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            raise Exception("Invalid data type")
        else:
            if self.denominator == other.denominator:
                return RationalNumber.reduced_form((self.numerator - self.numerator), self.denominator)
            else:
                if self.denominator % other.denominator == 0:
                    denom = self.denominator / other.denominator
                    return RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) - (other.numerator * self.denominator)), denom)
                elif other.denominator % self.denominator == 0:
                    denom = other.denominator / self.denominator
                    return RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) - (other.numerator * self.denominator)), denom)
                else:
                    denom = self.denominator * other.denominator
                    return RationalNumber.reduced_form(
                        ((self.numerator * other.denominator) - (other.numerator * self.denominator)), denom)

    def print_float(self):
        return f"{float(self.numerator)} / {float(self.denominator)}"

    @staticmethod
    def reduced_form(x, y):
        for z in range(2, 10):
            if x % z == 0 and y % z == 0:
                x /= z
                y /= z
                return RationalNumber.reduced_form(x, y)
        return f"{x} / {y}"


frac_1 = RationalNumber(13, 4)
frac_2 = RationalNumber(34, 8)
print(frac_1 - frac_2)
# print(frac_2.print_float())
