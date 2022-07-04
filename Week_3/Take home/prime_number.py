import math


def prime_checker(number: int) -> str:
    for x in range(2, number):
        if number % x == 0:
            return f"{number} is not a prime number"
    return f"{number} is a prime number"


def return_prime_value(number: list):
    for x in number:
        for z in range(2, x):
            if x % z == 0:
                break
        else:
            print(x)
    return "Here are the prime numbers"


def prime_number_root(number: int):
    sqr = round(math.sqrt(number))

    for prime in range(2, sqr + 1):
        if number % prime == 0:
            return f"{number} is not a prime nuber"
    else:
        return f'{number} is a prime number'


print(return_prime_value(range(900,1900)))
