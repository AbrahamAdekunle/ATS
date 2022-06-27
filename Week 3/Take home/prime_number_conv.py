def prime_number_converter(numero_list: list):
    for k, x in enumerate(numero_list):
        if x != 0 and x != 1 and x % 2 == 0:
            numero_list[numero_list.index(x)] = 0

    for k, x in enumerate(numero_list):
        for y in range(2, x):
            if x != 0 and x != 1 and x % y == 0:
                numero_list[k] = 0

    for k, x in enumerate(numero_list):
        for y in range(2, x):
            if x != 0 and x != 1 and x % y != 0:
                numero_list[k] = 1
    print(numero_list)
    return prime_conv_binar(numero_list)


def prime_conv_binar(numero_1:list):
    for k,v in enumerate(numero_1):
        if k >= 2 and v == 1:
            for z,y in enumerate(numero_1[k:]):
                if z % k == 0:
                    numero_1[z] = 0
                    break

    return numero_1



print(prime_number_converter(list(range(1000))))
