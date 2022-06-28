import csv
import sys
import pandas as pd


class SignUpSignIn:
    # details = []
    header = ["firstname", "lastname", "username", "password", "phone_number", "address", "Date_of_birth", "gender"]

    def __init__(self):
        self.field = {}

    @staticmethod
    def store_data():
        with open("csv_redo.csv", "r") as x:
            csv_reader = csv.DictReader(x)
            return list(csv_reader)

    def sign_up(self):
        self.field["firstname"] = SignUpSignIn.validate_firstname()
        self.field["lastname"] = SignUpSignIn.validate_lastname()
        self.field["username"] = SignUpSignIn.validate_username()
        self.field["password"] = SignUpSignIn.validate_password()

        # checker = SignUpSignIn.store_data()

        with open('csv_redo.csv', "a", newline="\n") as f:
            writer = csv.DictWriter(f, fieldnames=SignUpSignIn.header)
            # writer.writeheader()
            writer.writerow(self.field)

        print(f'To complete the process, you need to sign in')
        return SignUpSignIn.sign_in(self)

    def sign_in(self):
        checker = SignUpSignIn.store_data()
        username = input("kindly input your username")
        pass_word = input("kindly input your password")

        for rows in checker:
            if username == rows["username"] and pass_word == rows["password"]:
                print("Sign in succesful")
                return SignUpSignIn.successful(self)
        print("invalid details")
        return SignUpSignIn.sign_in(self)

    def successful(self):
        print(
            f'what would you like to do,today \n(1) Edit profile \n(2) change password \n(3) log out  \n kindly input the number of your choice')
        choice = input()

        if choice == "1":
            return SignUpSignIn.edit_profile(self)
        elif choice == '3':
            return SignUpSignIn.intro(self)
        elif choice == '2':
            return SignUpSignIn.change_password(self)
        print("Error! Invalid input")
        return SignUpSignIn.successful(self)

    def edit_profile(self):
        username = input("Enter your username")
        passw = input("kindly input your correct password")
        data = SignUpSignIn.store_data()
        for k, x in enumerate(data):

            if username == x["username"] and passw == x["password"]:
                p_numb = SignUpSignIn.validate_phone(self)

                addr = SignUpSignIn.validate_address(self)

                gend = SignUpSignIn.validate_gender(self)

                birthday = SignUpSignIn.d_o_b(self)

                df = pd.read_csv("csv_redo.csv")
                df.loc[k, "phone_number"] = p_numb
                df.loc[k, "address"] = addr
                df.loc[k, "gender"] = gend
                df.loc[k, "Date_of_birth"] = birthday
                df.to_csv("csv_redo.csv", index=False)

                print(" Edit successful")
                return SignUpSignIn.successful(self)

        print("Error! username and password doesn't exist ")
        return SignUpSignIn.sign_in(self)

    def change_password(self):
        username = input("kindly input your correct username")
        old = input("kindly input your former password")
        pass_word = input("input a new password , must be greater than 6 characters ")
        re_password = input("confirm the password you entered")

        data = SignUpSignIn.store_data()
        for k, x in enumerate(data):
            if pass_word == re_password and len(pass_word) >= 7 and username == x["username"] and old == x["password"]:
                print("correct passwords")
                df = pd.read_csv("csv_redo.csv.csv")
                df.loc[k, "password"] = pass_word
                df.to_csv("csv_redo.csv", index=False)
                print("change successful")
                return SignUpSignIn.successful(self)

        print("Error! invalid details")
        return SignUpSignIn.change_password(self)

    def validate_firstname(self):
        first_name = input("kindly input your firstname")
        if first_name.isalpha():
            return first_name
        print("invalid firstname")
        return SignUpSignIn.validate_firstname(self)

    def validate_lastname(self):
        last_name = input("kindly input your lastname")
        if last_name.isalpha():
            return last_name
        print("invalid lastname")
        return SignUpSignIn.validate_lastname(self)

    def validate_username(self):
        user_name = input("kindly input your username \n")
        if len(user_name) > 5:
            return user_name
        print("invalid username")
        return SignUpSignIn.validate_username(self)

    def validate_password(self):
        pass_word = input("input a unique password , must be greater than 6 characters ")
        re_password = input("confirm the password you entered")

        if pass_word == re_password and len(pass_word) >= 7:
            print("successful")
            return pass_word
        print("Error! invalid password format or password doesnt match")
        return SignUpSignIn.validate_password(self)

    def validate_phone(self):
        p_number = input(
            'Kindly type the new phone number , (add your country code and omit the first zero in your phone number) ')
        if len(p_number) == 14 and p_number.startswith('+'):
            print("succesful")
            return p_number
        return SignUpSignIn.validate_phone(self)

    def validate_address(self):
        add = input("kindly input your address(optional), if you dont want to, kindly hit the 'enter' key")
        return add

    def validate_gender(self):
        gen = (input("what is your gender, (1) Male (2) Female (3) LGBTQ-confused lots"))
        if gen == '1':
            return "Male"
        elif gen == '2':
            return 'Female'
        elif gen == '3':
            return "LGBTQ-confused lots"
        else:
            print('Error! Wrong input')
            return SignUpSignIn.validate_gender(self)

    def d_o_b(self):
        date = input("kindly input your date of birth in the format, 13-01-1994 \n")

        if not date.isalpha() or not date.isalnum() or not date.isdecimal() or not 8 < len(date) > 10:
            return date
        print("wrong format , kindly follow the instructions")
        return SignUpSignIn.d_o_b(self)

    def intro(self):
        u_input = input(
            "Enter (1) if you will like to sign in, (2) if you will like to sign up.......press any other key to exit \n")
        if u_input == "1":
            return SignUpSignIn.sign_in(self)
        elif u_input == "2":
            return SignUpSignIn.sign_up(self)
        else:
            sys.exit()


SignUpSignIn().intro()
# s.header_for_csv()
