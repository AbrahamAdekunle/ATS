def quadratic(a:int, b:int, c:int) ->str:
    product = a * c
    fact_list = []
    sum_of_factor = []
    if product > 0:
        for item in range(-(product), (product) +1):
            if item != 0 and product % item == 0:
                fact_list.append(item)
    elif product < 0:
        for item in range(product, (abs(product)) + 1 ):
            if item != 0 and product % item == 0:
                fact_list.append(item)
    else:
        print("product can't be zero, hence this is not a quadratic equation")

    # print(fact_list)


    for item_1 in fact_list:
        for item_2 in fact_list:
            if item_1 + item_2 == b:
                sum_of_factor.append(item_1)
                # break
                # sum_of_factor.append(item_2)
    # print(sum_of_factor)

    if a == 1 and len(sum_of_factor) == 1:
        return f"X1 = {-(sum_of_factor[0])}, and X2 ={-(sum_of_factor[0])}"
    elif a == 1 and len(sum_of_factor) == 2:
        return f"X1 = {-(sum_of_factor[0])}, and X2 = {-(sum_of_factor[1])}"
    elif a > 1 and len(sum_of_factor) == 2:
        return f"X1 = {-(sum_of_factor[0]) / a}, and X2 ={-(sum_of_factor[1]) / a}"
    elif a < 0 and len(sum_of_factor) == 1:
        return f"X1 = {-(sum_of_factor[0]) / a}, and X2 = {-(sum_of_factor[0]) / a}"
    elif a < 0 and len(sum_of_factor) == 2:
        return f"X1 = {-(sum_of_factor[0]) / a}, and X2 = {-(sum_of_factor[1]) / a}"




print(quadratic(1,-7,-10))