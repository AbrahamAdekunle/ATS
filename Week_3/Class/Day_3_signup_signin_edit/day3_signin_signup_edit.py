import csv
import sys
import time
import pandas as pd

head_king = ["firstname", "lastname", "username", "password", "phone_number", "address", "Date_of_birth", "gender"]


# with open("day_3.csv", 'a', newline='\n') as x:
#     csv_stuff = csv.DictWriter(x, fieldnames=head_king)
#     csv_stuff.writeheader()


# Sign-up Functions
def sign_up():
    # print(validate_firstname())
    f_name = validate_firstname()

    # print(validate_lastname())
    l_name = validate_lastname()

    # print(validate_username())
    u_name = validate_username()

    # print(validate_password())
    p_word = (validate_password())

    store_data_csv(firstname=f_name, lastname=l_name, username=u_name, password=p_word)

    print(f'To complete the process, you need to sign in,{f_name}')
    return sign_in()


def validate_firstname():
    first_name = input("kindly input your firstname")
    if first_name.isalpha():
        return first_name
    print("invalid firstname")
    return validate_firstname()


def validate_lastname():
    last_name = input("kindly input your lastname")
    if last_name.isalpha():
        return last_name
    print("invalid lastname")
    return validate_lastname()


def validate_username():
    user_name = input("kindly input your username \n")
    if len(user_name) > 5:
        return user_name
    print("invalid username")
    return validate_username()


def validate_password():
    pass_word = input("input a unique password , must be greater than 6 characters ")
    re_password = input("confirm the password you entered")

    if pass_word == re_password and len(pass_word) >= 7:
        print("successful")
        return pass_word
    print("Error! invalid password format or password doesnt match")
    return validate_password()


# CSV function
def store_data_csv(**update):
    with open("day_3.csv", 'a', newline='\n') as x:
        csv_stuff = csv.DictWriter(x, fieldnames=head_king)
        # csv_stuff.writeheader()
        csv_stuff.writerow(update)


def fetch_data():
    with open("day_3.csv", 'r+') as y:
        csv_fetch = csv.DictReader(y)
        return list(csv_fetch)


# def update_edit(**up):
#     data = fetch_data()
#     for z in data:
#         with open("day_3.csv", 'a') as x:
#             csv_stuff = csv.DictWriter(x, fieldnames=head_king)
#             csv_stuff.writerow(up)


# def update_password_csv(username, old_password, new_password):
#     with open("day_3.csv", "r") as z:
#         csv_update = csv.reader(z)
#
#     for edit in csv_update:
#         with open("day_3.csv", "a") as x:
#             csv_edit = csv.DictWriter(x)


# Signin function
def sign_in():
    # global rows
    username = input("kindly input your username")
    password = input("kindly input your password")

    d_base = fetch_data()
    for rows in d_base:
        if username == rows['username'] and password == rows["password"]:
            print("sign in successful")
            # time.sleep(2.1)
            return successful()
    print("invalid details")
    return sign_in()


def successful():
    print(
        f'what would you like to do,today \n(1) Edit profile \n(2) change password \n(3) log out  \n kindly input the number of your choice')
    choice = input()

    if choice == "1":
        return edit_profile()
    elif choice == '3':
        return intro()
    elif choice == '2':
        return change_password()
    print("Error! Invalid input")
    return successful()


def validate_phone():
    p_number = input(
        'Kindly type the new phone number , (add your country code and omit the first zero in your phone number) ')
    if len(p_number) == 14 and p_number.startswith('+'):
        print("succesful")
        return p_number
    return validate_phone()


def validate_address():
    add = input("kindly input your address(optional), if you dont want to, kindly hit the 'enter' key")
    return add


def validate_gender():
    gen = (input("what is your gender, (1) Male (2) Female (3) LGBTQ-confused lots"))
    if gen == '1':
        return "Male"
    elif gen == '2':
        return 'Female'
    elif gen == '3':
        return "LGBTQ-confused lots"
    else:
        print('Error! Wrong input')
        return validate_gender()


def d_o_b():
    date = input("kindly input your date of birth in the format, 13-01-1994 \n")

    if not date.isalpha() or not date.isalnum() or not date.isdecimal() or not 8 < len(date) > 10:
        return date
    print("wrong format , kindly follow the instructions")
    return d_o_b()


def edit_profile():
    # global head_king
    username = input("Enter your username")
    passw = input("kindly input your correct password")
    data = fetch_data()
    update = []
    for k, x in enumerate(data):

        if username == x["username"] and passw == x["password"]:
            p_numb = validate_phone()

            addr = validate_address()

            gend = validate_gender()

            birthday = d_o_b()

            df = pd.read_csv("day_3.csv")
            df.loc[k, "phone_number"] = p_numb
            df.loc[k, "address"] = addr
            df.loc[k, "gender"] = gend
            df.loc[k, "Date_of_birth"] = birthday
            df.to_csv("day_3.csv", index=False)

            print(" Edit successful")
            return successful()

            # update.append(x)

            # for details in update:
            #     with open("day_3.csv", "w") as kol:
            #         zoo = csv.DictWriter(kol, fieldnames=head_king)
            #         zoo.writeheader()
            #         zoo.writerows(update)
            #
            #         print("edit successful")3
            #         return successful()

            # with open("day_3.csv", 'a+') as k:
            #     zu = csv.DictWriter(k, fieldnames=head_king)
            #     zu.writerow({"firstname": x["firstname"], "lastname": x["lastname"], "username": x["username"],
            #                  "password": x["password"], "phone_number": phone_number, "address": addr,
            #                  "Date_of_birth": date_of_birth, "gender": gender})
            #     print("Edit successful")
            #
            #     # edit_list = []
            #     with open('day_3.csv', 'a+')as s:
            #         ru = csv.DictReader(s)
            #         for row in ru:
            #             if row['firstname'] == x['username']:
            #                 dele = csv.DictWriter(s)
            #
            #
            #             # for field in row:
            #             #     if field == x['firstname']:
            #             #         edit_list.remove(row)
            #
            #     # with open("day_3.csv", 'a') as lo:
            #     #     loki = csv.DictWriter(lo, fieldnames=head_king)
            #     #     loki.writerows(edit_list)
            #     # return successful()
    print("Error! username doesn't exist ")
    return sign_in()

    # update_edit(phone_number=phone_number, address=addr, gender=gender, Date_of_birth=date_of_birth)


def change_password():
    username = input("kindly input your correct username")
    old = input("kindly input your former password")
    pass_word = input("input a new password , must be greater than 6 characters ")
    re_password = input("confirm the password you entered")

    data = fetch_data()
    for k, x in enumerate(data):
        if pass_word == re_password and len(pass_word) >= 7 and username == x["username"] and old == x["password"]:
            print("correct passwords")
            df = pd.read_csv("day_3.csv")
            df.loc[k, "password"] = pass_word
            df.to_csv("day_3.csv", index=False)
            print("change successful")
            return successful()

    print("Error! invalid details")
    return change_password()


# Entry point function
def intro():
    u_input = input(
        "Enter (1) if you will like to sign in, (2) if you will like to sign up.......press any other key to exit \n")
    if u_input == "1":
        return sign_in()
    elif u_input == "2":
        return sign_up()
    else:
        sys.exit()


print(intro())
