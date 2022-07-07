number_list = [1 for number in range(1000)]


def subscript_prime(number_list: list) -> list:
    for k, v in enumerate(number_list):
        if k == 0 or k == 1 or k == 2:
            number_list[k] = 1
        elif k > 2:
            for numero in range(2, k):
                if k % numero == 0:
                    number_list[k] = 0
                    break
    print(number_list)


def multiple_subscript_prime(num_list: list):
    for k, v in enumerate(num_list):
        if k == 0 or v == 0:
            continue
        elif k >= 2 and v == 1:
            for number in range((k+1), len(num_list)):
                if number % k == 0:
                    num_list[number] = 0
    print(num_list)


#
#
test = subscript_prime(number_list)
