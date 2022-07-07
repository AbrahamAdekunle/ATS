import random
import string


class Wallet:
    # States the number of users created
    counter = 0
    for_id = string.ascii_uppercase
    for_pin = string.digits
    details = []

    def __init__(self, firstname: str, lastname: str, ):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__username = firstname[0].upper() + lastname[0:2].upper() + "".join(random.sample(Wallet.for_pin, 3))
        self.__pin = "".join(random.sample(Wallet.for_pin, 4))
        self.balance = 0

        Wallet.counter += 1
        Wallet.details.append(self)

    def __repr__(self):
        return f"Wallet({self.firstname}, {self.lastname}, {self.username}, {self.pin},{self.balance})"

    # def delete_profile(self):

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if len(value) > 15:
            raise ValueError(f"{value} is too long")
        elif value == self.__firstname:
            raise   ValueError(f"{value} is the same as previous username")
        elif len(value) < 15 and value != self.__firstname:
            self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if len(value) > 15:
            raise ValueError(f"{value} is too long")
        elif value == self.__lastname:
            raise ValueError(f"{value} is the same as previous username")
        elif len(value) <= 15 and value != self.__lastname:
            self.__lastname = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) > 15:
            raise ValueError(f"{value} is too long")
        elif value == self.__username:
            raise ValueError(f"{value} is the same as previous username")
        elif len(value) <= 15 and value != self.__username:
            self.__username = value

    @property
    def pin(self):
        return self.__pin


class User(Wallet):
    def __init__(self, firstname, lastname):
        super().__init__(
            firstname, lastname
        )

    def fund_wallet(self, amount: int):
        if amount > 0:
            self.balance = self.balance + amount
            Transaction.transaction_log.append(f"{self.username},({amount} deposited by {self.firstname}, with the new "
                                               f"balance of {self.balance})")
            return f" Successful!, Your new balance is {self.balance}"
        return "Error! Invalid amount"


class Transaction(Wallet):
    transaction_log = []

    def __init__(self, firstname, lastname):
        super().__init__(
            firstname, lastname
        )
        pass


wall_1 = Wallet('Chukwudi', 'Oduma')
wall_2 = Wallet('Davies', "Ayodele")
# user_1 = User('Chukwudi', 'Oduma').fund_wallet(200)
# user_2 = User('Davies', "Ayodele").fund_wallet(300)
#
# print(Transaction.transaction_log)


# print(wall_1)

# to delete a profile
del wall_1

# print (wall_1)
