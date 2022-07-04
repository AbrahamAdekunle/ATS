import math

from tabulate import tabulate


def salesperson_recorder():
    list_name = []
    id_list = []

    list_product = [[], [], [], [], []]
    a = [[], [], [], [], []]
    b = [[], [], [], [], []]
    c = [[], [], [], [], []]
    d = [[], [], [], [], []]

    for x in range(4):
        name = validate_name()
        list_name.append(name)

        identity = validate_id_number()
        id_list.append(identity)

        for y in range(5):
            print(f"this is for product {y}")
            if x == 0:
                while True:
                    choice = validate_choice(y)
                    if choice == 12345:
                        break
                    elif choice > 0:
                        list_product[y].append(choice)
                        a[y].append(choice)
                    else:
                        print("invalid input....")
                        continue
            elif x == 1:
                while True:
                    choice = validate_choice(y)
                    if choice == 12345:
                        break
                    elif choice > 0:
                        list_product[y].append(choice)
                        b[y].append(choice)
                    else:
                        print("invalid input....")
                        continue
            elif x == 2:
                while True:
                    choice = validate_choice(y)
                    if choice == 12345:
                        break
                    elif choice > 0:
                        list_product[y].append(choice)
                        c[y].append(choice)
                    else:
                        print("invalid input....")
                        continue
            elif x == 3:
                while True:
                    choice = validate_choice(y)
                    if choice == 12345:
                        break
                    elif choice > 0:
                        list_product[y].append(choice)
                        d[y].append(choice)
                    else:
                        print("invalid input....")
                        continue

        a_sum = sum((sum(a[0]), sum(a[1]), sum(a[2]), sum(a[3], sum(a[4]))))
        b_sum = sum((sum(b[0]), sum(b[1]), sum(b[2]), sum(b[3], sum(b[4]))))
        c_sum = sum((sum(c[0]), sum(c[1]), sum(c[2]), sum(c[3], sum(c[4]))))
        d_sum = sum((sum(d[0]), sum(d[1]), sum(d[2]), sum(d[3], sum(d[4]))))
        t_sum = sum((sum(list_product[0]), sum(list_product[1]), sum(list_product[2]), sum(list_product[3]), sum(list_product[4])))

    sales_table = [[list_name[0],list_name[1], list_name[2], list_name[3], "Sum of specific products sold"],
                   [sum(a[0]), sum(b[0]), sum(c[0]), sum(d[0]), sum(list_product[0])],
                   [sum(a[1]), sum(b[1]), sum(c[1]), sum(d[1]), sum(list_product[1])],
                   [sum(a[2]), sum(b[2]), sum(c[2]), sum(d[2]), sum(list_product[2])],
                   [sum(a[3]), sum(b[3]), sum(c[3]), sum(d[3]), sum(list_product[3])],
                   [sum(a[4]), sum(b[4]), sum(c[4]), sum(d[4]), sum(list_product[4])],
                   [a_sum, b_sum, c_sum, d_sum, t_sum]]

    return tabulate(sales_table, headers="firstrow", tablefmt="fancy_grid", showindex=range(4))
    # print("SALES".center(30, "="))
    # print(" " + "|" + list_name[0] + "|" + list_name[1] + "|" + list_name[2] + "|" + list_name[
    #     3] + "|" + "Sum of products sold")
    # print(f"0" + "|" + str(sum(a[0])) + "|" + str(sum(b[0])) + "|" + str(sum(c[0])) + "|" + str(sum(d[0])) + "|" + str(
    #     sum(list_product[0])))
    # print("1" + "|" + str(sum(a[1])) + "|" + str(sum(b[1])) + "|" + str(sum(c[1])) + "|" + str(sum(d[1])) + "|" + str(
    #     sum(list_product[1])))
    # print("2" + "|" + str(sum(a[2])) + "|" + str(sum(b[2])) + "|" + str(sum(c[2])) + "|" + str(sum(d[2])) + "|" + str(
    #     sum(list_product[2])))
    # print("3" + "|" + str(sum(a[3])) + "|" + str(sum(b[3])) + "|" + str(sum(c[3])) + "|" + str(sum(d[3])) + "|" + str(
    #     sum(list_product[3])))
    # print("4" + "|" + str(sum(a[4])) + "|" + str(sum(b[4])) + "|" + str(sum(c[4])) + "|" + str(sum(d[4])) + "|" + str(
    #     sum(list_product[4])))
    # print(" " + "|" + str(a_sum) + "|" + str(b_sum) + "|" + str(c_sum) + "|" + str(d_sum) + "|")
    # return "Done"


def validate_name():
    name = input("kindly input the salesperson name\n")
    if name.isalpha():
        return name
    print("invalid input")
    return validate_name()


def validate_id_number():
    identity = input("kindly input the ID of the salesperson\n")
    if identity.isdecimal():
        return identity
    return validate_id_number()


def validate_choice(y):
    choice = (input(f"Kindly input the figure sold for product {y}, if done, enter 12345 to to "
                    f"move to the next product \n "))
    if choice.isdecimal():
        return int(choice)
    print("invalid input")
    return validate_choice(y)


print(salesperson_recorder())
