import csv
import random
import string
import sys
import pandas as pd


class SignUpSignIn:
    # details = []
    header = ["firstname", "lastname", "username", "password", "User_ID", "phone_number", "address", "Date_of_birth",
              "gender"]
    for_id = string.digits

    def __init__(self):
        self.field = {}

    @staticmethod
    def store_data():
        with open("csv_redo.csv", "r") as x:
            csv_reader = csv.DictReader(x)
            return list(csv_reader)

    def sign_up(self):
        self.field["firstname"] = SignUpSignIn.validate_firstname(self)
        self.field["lastname"] = SignUpSignIn.validate_lastname(self)
        self.field["username"] = SignUpSignIn.validate_username(self)
        self.field["password"] = SignUpSignIn.validate_password(self)
        self.field["User_ID"] = "".join(random.sample(SignUpSignIn.for_id, 5))

        # checker = SignUpSignIn.store_data()

        with open('csv_redo.csv', "a", newline="\n") as f:
            writer = csv.DictWriter(f, fieldnames=SignUpSignIn.header)
            if len(SignUpSignIn.store_data()) < 1:
                writer.writeheader()
                writer.writerow(self.field)
            else:
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


class GetProfile(SignUpSignIn):
    def __init__(self, userid):
        super().__init__()
        self.__userid = userid

        for profile in SignUpSignIn.store_data():
            if profile["User_ID"] == userid:
                self.__firstname = profile["firstname"]
                self.__lastname = profile["lastname"]
                self.__password = profile["password"]
                self.__phone_number = profile["phone_number"]
                self.__address = profile["address"]
                self.__D_O_B = profile["Date_of_birth"]
                self.__gender = profile['gender']
                break

    @property
    def userid(self):
        return self.__userid

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, value):
        if value.isalpha() and len(value) > 2:
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "firstname"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    self.__firstname = value
                    print("firstname Updated Successfully")
                    break
        elif value.isalnum():
            raise ValueError("Error! Invalid value")

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, value: str):
        if value.isalpha() and len(value) > 2:
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "lastname"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    self.__lastname = value
                    print("lastname Updated Successfully")
                    break
        elif value.isalnum():
            raise ValueError("Error! Invalid value")

    def get_password(self):
        return self.__password

    def set_password(self, value):
        if len(value) >= 7:
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "password"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    self.__password = value
                    print("Password Updated Successfully")
                    break
        else:
            raise ValueError("Error! Invalid Password (less than 7 characters")

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, value: str):
        if len(value) == 14 and value.startswith("+"):
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "phone_number"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    print("Phone Number Updated Successfully")
                    self.__phone_number = value
                    break
        else:
            raise ValueError('Error!, Invalid phone number')

    def get_address(self):
        return self.__address

    def set_address(self, value):
        for k, v in enumerate(SignUpSignIn.store_data()):
            if self.userid == v["User_ID"]:
                df = pd.read_csv("csv_redo.csv")
                df.loc[k, "address"] = value
                df.to_csv("csv_redo.csv", index=False)
                self.__address = value
                print("Address Updated Successfully")
                break

    def get_gender(self):
        return self.__gender

    def set_gender(self, value: str):
        value = value.capitalize()
        if value == "Male" or value == "Female":
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "gender"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    self.__gender = value
                    print("Gender Updated Successfully")
                    break
        else:
            raise ValueError("Error! Invalid gender")

    def get_date_of_birth(self):
        return self.__D_O_B

    def set_date_of_birth(self, value: str):
        if 8 < len(value) < 11 and value.count("-") == 2:
            for k, v in enumerate(SignUpSignIn.store_data()):
                if self.userid == v["User_ID"]:
                    df = pd.read_csv("csv_redo.csv")
                    df.loc[k, "Date_of_birth"] = value
                    df.to_csv("csv_redo.csv", index=False)
                    self.__D_O_B = value
                    print("Date of birth Updated Successfully")
                    break
        else:
            raise ValueError("Error! Invalid parameters")

    firstname = property(fget=get_firstname, fset=set_firstname)
    lastname = property(fget=get_lastname, fset=set_lastname)
    password = property(fget=get_password, fset=set_password)
    phone_number = property(fget=get_phone_number, fset=set_phone_number)
    address = property(fget=get_address, fset=set_address)
    D_O_B = property(fget=get_date_of_birth, fset=set_date_of_birth)
    gender = property(fget=get_gender, fset=set_gender)

# SignUpSignIn().sign_in()
# s.header_for_csv()

profile1 = GetProfile("31482")
print(profile1.D_O_B)
profile1.D_O_B = "13-01-1996"
print(profile1.D_O_B)
# print(profile1.gender)
# print(profile1.password)
# print(profile1.userid)
# print(profile1.phone_number)
# print(profile1.address)
