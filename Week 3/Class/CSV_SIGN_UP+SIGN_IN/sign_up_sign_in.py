import csv
import sys

with open("signin_up.csv", "r") as xu:
    hand = csv.DictReader(xu)
    for rows in hand:
        print()


def sign_in():
    global rows
    user = input("kindly input your username \n")
    p_w_o = input("kindly enter your password \n")

    if user == rows['username'] and p_w_o == rows['password']:
        return 'login is successful, welcome'
    print("invalid log-in details")
    return sign_in()


wel_c = int(input("Enter (1) to sign in or (2) to sign up \n"))

if wel_c == 1:
    print(sign_in())
elif wel_c == 2:
    f_name = input("input your firstname \n")
    l_name = input("input your lastname \n")

    while True:
        u_name = input("kindly input a username \n")
        if 5 < len(u_name) < 15:
            print("username accepted")
            break
        else:
            print("invalid username")
            continue

    for x in range(0, 3):
        p_word = input("kindly input a unique password (must be more than 8 characters, and can contain mixture of "
                       "alphanumerical and special characters)\n")
        p_word_conf = input("kindly re-type your password \n")

        if p_word == p_word_conf and len(p_word) >= 8:
            print("Details-set successfully")
            break
        else:
            print("invalid password format")
            continue

    with open('signin_up.csv', 'w') as you:
        head_king = ["firstname", "lastname", "username", "password"]
        zoo = csv.DictWriter(you, fieldnames=head_king)
        zoo.writeheader()
        zoo.writerow({
            "firstname": f_name,
            "lastname": l_name,
            "username": u_name,
            "password": p_word
        })
else:
    sys.exit()







# with open("signin_up.csv", "r") as xu:
#     hand = csv.DictReader(xu)
#     for rows in hand:
#         print(rows)

#     f_name = input("input your firstname \n")
#     l_name = input("input your lastname \n")
#
#     while True:
#         u_name = input("kindly input a username \n")
#         if 5 < len(u_name) < 15:
#             break
#         else:
#             print("invalid username")
#             continue
#
#     for x in range(0, 3):
#         p_word = input("kindly input a unique password (must be more than 8 characters, and can contain mixture of "
#                     "alphanumerical and special characters)\n")
#         p_word_conf = input("kindly re-type your password \n")
#
#         if p_word == p_word_conf and len(p_word) >= 8:
#             break
#         else:
#             print("invalid password format")
#             continue
#
#     with open('signin_up.csv', 'w') as you:
#         head_king = ["firstname", "lastname", "username", "password"]
#         zoo = csv.DictWriter(you, fieldnames=head_king)
#         zoo.writeheader()
#         zoo.writerow({
#             "firstname": f_name,
#             "lastname": l_name,
#             "username": u_name,
#             "password": p_word
#         })
#
#     with open("signin_up.csv", "r") as xu:
#         hand = csv.DictReader(xu)
#         for rows in hand:
#             print(rows)
#
#
# def sign_in():
#     global rows
#     user = input("kindly input your username \n")
#     p_w_o = input("kindly enter your password \n")
#
#     if user == rows['firstname'] and p_w_o == rows['password']:
#         return 'login is successful, welcome'
#     print("invalid log-in details")
#     return sign_in()
