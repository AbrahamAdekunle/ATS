def addnums(x, y=0):
    return f"the answer is {x + y}"


def subtract(x, y=0):
    return f" the answer is {x - y}"


def multiply(x, y=0):
    return f" the answer is {x * y}"


def divide(x, y=1):
    return f" the answer is {x / y}"


while True:
    first_int = input("input the first integer \n")
    operator = input("what is the operator sign \n")
    second_int = input("what is the second integer \n")

    try:
        first_int = int(first_int)
        second_int = int(second_int)

    except:
        print("please input numeric digits")
        continue

    if operator == '+':
        print(addnums(first_int, second_int))
        break
    elif operator == "-":
        print(subtract(first_int, second_int))
        break
    elif operator == '*':
        print(multiply(first_int, second_int))
        break
    elif operator == '/':
        if second_int == 0 :
            print("can't divide by zero")
        else:
            print(divide(first_int, second_int))
        break
    else:
        print("invalid operator")
        continue
