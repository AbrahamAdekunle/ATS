import sys
import random
import string

password_lc = string.ascii_lowercase
password_uc = string.ascii_uppercase
password_digits = string.digits
password_symbol = string.punctuation

ussd_dict = {
    "*901#": "Access bank",
    '*326#': "EcoBank",
    "*770#": "Fidelity bank",
    "*894#": "First bank",
    '*389*214#': "FCMB",
    "*737#": 'GTB',
    "*966#": "Zenith bank",
    "*945#": "wema bank",
    "*919#": "UBA"
}


def transaction_progressing():
    # print(f"For the basis of this particular session, here is your pin, {pin}")
    for i in range(3, 0, -1):
        input_pin = int(input("kindly type your pin  "))
        if pin == input_pin:
            print(
                f"what would you like to do today,{name} : (1) > Get balance, (2) > Make a transfer, (3) > "
                f"Load airtime, (4) > Load DATA, (5) > Generate OTP")
            task_input = int(input())
            if task_input == 1:
                print(get_balance())
                print(any_more_transaction())
                sys.exit()
            elif task_input == 2:
                print(transfer())
                print(any_more_transaction())
                sys.exit()
            elif task_input == 3:
                print(airtime())
                print(any_more_transaction())
                sys.exit()
            elif task_input == 4:
                print(data())
                print(any_more_transaction())
                sys.exit()
            elif task_input == 5:
                print(one_time_password())
                print(any_more_transaction())
                sys.exit()
            else:
                return "invalid input"

        else:
            print(f'wrong pin,try again...you have {i - 1} tries left')
            continue
    sys.exit()


def get_balance():
    return 'your balance would be sent to your e-mail and your registered mobile number'


def transfer():
    amount = int(input('how much would you like to transfer ? '))

    for z in range(3, 0, -1):
        if amount <= 20000:
            for y in range(3, 0, -1):
                recipient = input("kindly input the recipient's account number")
                if len(recipient) == 10:
                    insert_pin = int(input('kindly insert your 4-digit pin'))
                    if insert_pin == pin:
                        return 'Transaction successful'
                    else:
                        return 'wrong pin'

                else:
                    print(f"wrong account number, kindly recheck....you have {y - 1} tries left")
                    continue
            sys.exit()
        else:
            print(f"amount greater than #20,000, please reduce it....you have {(z - 1)} tries left")
            continue
    sys.exit()


def airtime():
    for z in range(3, 0, -1):
        choice = int(input("who do you want to load the airtime for : (1) > Self  (2) > others"))
        if choice == 1:
            for y in range(3, 0, -1):
                numero = int(input('how much airtime would you like to load'))
                if numero <= 20000:
                    insert_pin = int(input("kindly insert your pin"))
                    if pin == insert_pin:
                        return "Transaction successful"
                    else:
                        return 'incorrect pin'
                else:
                    print("the amount is greater than 20000, kindly reduce it.....you have{(y)-1} tries left")
                    continue
            sys.exit()

        elif choice == 2:
            for y in range(3, 0, -1):
                numero = int(input('how much airtime would you like to load '))
                if numero <= 20000:
                    for a in range(3, 0, -1):
                        insert_number = input("kindly insert phone number ")
                        if len(insert_number) == 11:
                            insert_pin = int(input("kindly insert your pin "))
                            if pin == insert_pin:
                                return "Transaction successful"
                            else:
                                return 'incorrect pin'
                        else:
                            print(f'invalid phone number, kindly check the number.....you have {a - 1} tries left')
                            continue
                    sys.exit()
                else:
                    print("the amount is greater than 20000, kindly reduce it.....you have{(y)-1} tries left")
                    continue
            sys.exit()

        else:
            print("invalid input, kindly re-check.....you have {(z) - 1} tries left")
            continue
    sys.exit()


def one_time_password():
    o_t_p = random.choice(password_digits) + random.choice(password_uc) + random.choice(password_lc) + random.choice(
        password_symbol)
    return o_t_p


def data():
    for x in range(3, 0, -1):
        choice = int(input("who would you like to get the data for ? (1) > self (2) > others "))
        if choice == 1:
            for y in range(3, 0, -1):
                numero = int(input('how much data would you like to load'))
                if numero <= 20000:
                    insert_pin = int(input("kindly insert your pin"))
                    if pin == insert_pin:
                        return "Transaction successful"
                    else:
                        return 'incorrect pin'
                else:
                    print("the amount is greater than 20000, kindly reduce it.....you have{(y)-1} tries left")
                    continue
            sys.exit()

        elif choice == 2:
            for y in range(3, 0, -1):
                numero = int(input('how much data would you like to load'))
                if numero <= 20000:
                    for a in range(3, 0, -1):
                        insert_number = int(input("kindly insert phone number"))
                        if insert_number == 11:
                            insert_pin = int(input("kindly insert your pin"))
                            if pin == insert_pin:
                                return "Transaction successful"
                            else:
                                return 'incorrect pin'
                        else:
                            print(f'invalid phone number, kindly check the number.....you have {a - 1} tries left')
                            continue
                    sys.exit()
        else:
            print('invalid input...kindly re-check...you have {x-1} tries left')
            continue
        sys.exit()


def any_more_transaction():
    for g in range(3, 0, -1):
        choice = int(input("would you like to make another transaction, (1) > YES, (2) > NO "))
        if choice == 1:
            return transaction_progressing()
        elif choice == 2:
            return 'Thank you for banking with us'
        else:
            print(f"invalid input,...kindly re-check your input....you have {g - 1} tries left")
            continue
    sys.exit()


# generated_pin = random.choice(password_digits) + random.choice(password_digits) + random.choice(password_digits) + random.choice(password_digits)

name = input("Welcome User, what is your name ? ")
print(f"Welcome, {name.title()}")

for x in range(3, 0, -1):
    ussd_code = input(f"{name.title()}, please input the USSD code of your bank ")

    if ussd_code in ussd_dict.keys():
        print(f"""
            Welcome to {ussd_dict[ussd_code]},{name.title()}.. 
        before you proceed ,you'll be charged 6.98 for your transactions, 
        if your agree, press (1), if you dont, press (2 )
                """)
        ussd_p_input = int(input())

        if ussd_p_input == 1:
            for q in range(3, 0, -1):
                print("You need to set a pin")
                pin_1 = str(input())
                if len(pin_1) == 4 and pin_1.isdecimal():
                    print('you have set a 4-digit, make sure to keep it secure and dont tell anyone, ')
                    pin = int(pin_1)
                    print(transaction_progressing())
                    sys.exit()
                else:
                    print("wrong format....your pin has to be 4_digits")
                    print(f'you have {q-1} tries left ')
            print('You no dey hear word....oya commot for here')
            sys.exit()


        else:
            print('Thank you')
            sys.exit()

    else:
        print(f"incorrect USSD, kindly re-check....you have {x - 1} tries left")
        continue
print('You no dey hear word....oya commot for here')
sys.exit()

