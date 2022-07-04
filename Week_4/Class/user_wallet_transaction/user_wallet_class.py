import csv
import datetime
import pandas
import random
import string
import sys


class User:
    for_pin = string.digits
    for_id = string.ascii_uppercase
    head_king = ["Firstname", "Middlename", "Lastname", "username", "phone number", "wallet_ID", "pin", "balance"]
    header_transaction = ["Date", "wallet_ID", "Narration", "credits", "debits", "Balance"]
    date = datetime.date.today()

    def __init__(self):
        self.field = {}

    @staticmethod
    def get_data():
        with open("user_details.csv", "r") as x:
            reader = csv.DictReader(x)
            return list(reader)

    def user_registration(self):
        pin = "".join((random.sample(User.for_pin, 5)))
        wallet_id = "".join((random.sample(User.for_id, 3))) + "".join((random.sample(User.for_pin, 5)))

        self.field["Firstname"] = User.validate_firstname(self)
        self.field["Middlename"] = User.validate_middlename(self)
        self.field["Lastname"] = User.validate_lastname(self)
        self.field["username"] = User.validate_username(self)
        self.field["phone number"] = User.validate_phone(self)
        self.field["wallet_ID"] = wallet_id
        self.field["pin"] = pin
        self.field["balance"] = 0

        print(f"Here are ,your ID , {wallet_id}, and your pin {pin}, dont tell anyone")

        with open("user_details.csv", "a", newline="\n") as x:
            writer = csv.DictWriter(x, fieldnames=User.head_king)
            # writer.writeheader()
            writer.writerow(self.field)

        return "Registration Successful"

    def delete_user(self):

        data = User.get_data()
        user = input("kindly input your username\n")
        pin = input("kindly input your pin\n")

        for k, v in enumerate(User.get_data()):
            if v["username"] == user and v['pin'] == pin:
                print("You will be missed, GOODBYE!!")
                delete = pandas.read_csv("user_details.csv")
                delete.drop(k)
                delete.to_csv("user_wallet.csv", index=False)
                print("Deletion Successful")
            elif v["username"] != user and v['pin'] != pin:
                print("Invalid Details!!")
                sys.exit()

    def validate_firstname(self):
        first_name = input("kindly input your firstname\n")
        if first_name.isalpha():
            return first_name
        print("invalid firstname")
        return User.validate_firstname(self)

    def validate_lastname(self):
        last_name = input("kindly input your lastname\n")
        if last_name.isalpha():
            return last_name
        print("invalid lastname")
        return User.validate_lastname(self)

    def validate_middlename(self):
        middlename = input("kindly input your middlename\n")
        if middlename.isalpha():
            return middlename
        print("invalid firstname")
        return User.validate_middlename(self)

    def validate_username(self):
        user_name = input("kindly input your username \n")
        if len(user_name) > 5:
            return user_name
        print("invalid username")
        return User.validate_username(self)

    def validate_phone(self):
        p_number = input(
            'Kindly type your phone number , (add your country code and omit the first zero in your phone number) \n')
        if len(p_number) == 14 and p_number.startswith('+'):
            return p_number
        return User.validate_phone(self)


class Wallet(User):

    # def __init__(self, field):
    # super().__init__(field)
    # self.username = username
    # self.pin = pin

    def fund_wallet(self):
        amount = int(input("kindly input the amount you will like to add\n"))
        if amount < 0:
            print("invalid amount")
            Wallet.fund_wallet(self)

        # data = User.get_data()
        wallet = input("Kindly input your Wallet ID\n")
        pin = input("kindly input your pin\n")

        for k, x in enumerate(User.get_data()):
            if wallet == x["wallet_ID"] and pin == x["pin"]:
                print("correct Credentials!!")
                # transaction_id = wallet[0:3] + "".join(random.sample(User.for_pin, 10))
                Transaction.logging_transaction(Date=User.date, wallet_ID=wallet,
                                                Narration="Deposit(self)",
                                                credits=amount,
                                                Balance=(int(x["balance"]) + amount))
                print("Deposit Successful")

                df = pandas.read_csv("user_details.csv")
                df.loc[k, "balance"] = int(x["balance"]) + amount
                df.to_csv("user_details.csv", index=False)
                return "successful"

            elif wallet != x["wallet_ID"] or pin != x["pin"]:
                print("invalid details")
                sys.exit()

    def withdraw_funds(self):
        wallet = input("Kindly input your wallet ID")
        pin = input("kindly inout your pin")

        for k, x in enumerate(User.get_data()):
            if wallet == x["wallet_ID"] and pin == x["pin"]:
                print("correct Credentials!!")
                while True:
                    amount = int(input("Kindly enter the amount you will like to withdraw"))
                    if amount < int(x["balance"]):
                        break
                    else:
                        print("invalid amount")
                        continue

                while True:
                    aza = str(input("Kindly input the account number you will like to transfer funds to"))
                    if len(aza) == 10 and aza.isdecimal():
                        break
                    else:
                        continue
                choice = input(f"You are about to send {amount} to {aza}, are you sure your want to proceed,"
                               f"Enter (1) to confirm, press any other key to exit")
                if choice == "1":
                    transaction_id = wallet[0:3] + "".join(random.sample(User.for_pin, 10))
                    Transaction.logging_transaction(Date=User.date, wallet_ID=wallet,
                                                    Narration=f"{amount}, transferred to {aza}"
                                                    , debits=amount,
                                                    Balance=(int(x["balance"]) - amount))
                    df = pandas.read_csv("user_details.csv")
                    df.loc[k, "balance"] = int(x["balance"]) - amount
                    df.to_csv("user_details.csv", index=False)
                    return "transaction successful"
                else:
                    sys.exit()

            elif wallet != x["wallet_ID"] and pin != x["pin"]:
                print("invalid details")
                sys.exit()

    def get_balance(self):
        wallet = input("Kindly input your Wallet ID\n")
        pin = input("kindly input your pin\n")

        data = User.get_data()

        for x in data:
            if wallet == x["wallet_ID"] and pin == x["pin"]:
                print("valid details")
                print (f"{x['balance']}, is your balance as at {datetime.datetime.now()}")
            return "Error! Invalid details"


class Transaction(User):
    @staticmethod
    def logging_transaction(**kwargs):
        with open("transactions.csv", "a", newline="\n") as z:
            writer = csv.DictWriter(z, fieldnames=User.header_transaction)
            # writer.writeheader()
            writer.writerow(kwargs)


# Wallet().get_balance()
User().delete_user()
