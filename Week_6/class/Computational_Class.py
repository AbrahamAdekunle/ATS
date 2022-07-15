import math

import tabulate


class Computation(int):
    def __init__(self):
        pass

    def factorial(self):
        try:
            number = int(input("kindly input the integer \n"))
        except ValueError:
            print("Error! Input a number")
            return Computation.factorial(self)

        factorial_list = list(range(1, number + 1))
        print(f"The factorial of {number} is {math.prod(factorial_list)}")

    def sum(self):
        try:
            number = int(input("kindly input the integer \n"))
        except ValueError:
            print("Error! Input a number")
            return Computation.sum(self)

        sum_list = list(range(1, number + 1))
        print(f"The sum is {sum(sum_list)}")

    def test_prim(self):
        try:
            number = int(input("kindly input the integer \n"))
        except ValueError:
            print("Error! Input a number")
            return Computation.test_prim(self)

        if number > 1:
            for divisor in range(2, number):
                if number % divisor == 0:
                    print(f"{number} is not a prime number")
                    break
            else:
                print(f'{number} is a prime number')
        else:
            print(f"{number} is not a prime number")

    def tablemult(self):
        try:
            number = int(input("kindly input the integer \n"))
        except ValueError:
            print("Error! Input a number")
            return Computation.tablemult(self)

        index = []
        result = []

        for multiple_integers in range(21):
            index.append(multiple_integers)
            result.append(multiple_integers * number)

        print(tabulate.tabulate({" ": index, number: result}, headers="keys"))

    def alltablemult(self):
        try:
            number = int(input("kindly input the integer \n"))
        except ValueError:
            print("Error! Input a number")
            return Computation.alltablemult(self)

        for num in range(1, number + 1):
            text = f"Multiplication table of {num}"
            print(text.center(60,'*'))
            for numero in range(1,21):
                print(f"{num} * {numero} = {num * numero}")

    @staticmethod
    def listdiv(number):
        ldiv = []

        for divisor in range(1, number + 1):
            if number % divisor == 0:
                ldiv.append(divisor)
        print(f"The divisors are {ldiv}")
        return ldiv

    def listdivprime(self, number):
        # divisor_list = self.listdiv(number)

        ldivprime = []

        for integer in self.listdiv(number):
            if integer > 1 and integer % 2 != 0:
                for num in range(2, integer):
                    if integer % num == 0:
                        break
                else:
                    ldivprime.append(integer)
        print(f"the prime divisors are {ldivprime}")


Computation().alltablemult()
