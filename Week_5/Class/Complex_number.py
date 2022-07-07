import cmaths


class ComplexNumber:
    def __init__(self, x: float = 1.0, y: float = 1.0):
        self.complex = complex(x, y)

    def __repr__(self):
        return f"{self.complex}"

    def addition(self, other):
        if not isinstance(other, ComplexNumber):
            raise Exception("Error,invalid Data Type ")
        return f"the 'real' result is {self.complex.real + other.complex.real},  and the imaginary is {self.complex.imag + self.complex.imag}"

    def subtraction(self, other):
        if not isinstance(other, ComplexNumber):
            raise Exception("Error,invalid Data Type ")
        return f"the 'real' result is {self.complex.real - other.complex.real},  and the imaginary is {self.complex.imag - self.complex.imag}"

    def print_floating_number(self):
        return f"({self.complex.real} , {self.complex.imag})"


c = ComplexNumber(2, 3)
c2 = ComplexNumber(9, 3)
print(c.addition(c2))
