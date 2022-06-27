import random
import string


def no_duplicate():
    numero = string.digits

    checker = []
    for x in range(20):
        number = random.sample(numero, 3)
        if number not in checker:
            checker.append(number)
            print("".join(number))
        elif number in checker:
            number = random.sample(numero, 3)
            if number not in checker:
                checker.append(number)
                print("".join(number))

    return "Done"


print(no_duplicate())
