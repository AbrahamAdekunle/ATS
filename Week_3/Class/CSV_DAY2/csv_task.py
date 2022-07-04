import csv
import time

for x in range(0, 3):
    f_name = input("what is your first name ? \n")
    l_name = input("what is your last name ? \n")
    m_name = input("what is your middle name ? \n")
    age = input("what is your age ? \n")
    occupation = input("what is your occupation ? \n")
    d_o_b = input("what is your date of birth ? use this format (13-01-1996) \n")
    gender = input("what is your gender ? M or F \n")
    marital_status = input("what is your marital status \n")
    email = input('what is your email \n')

    # details = [f_name, l_name, m_name, age, occupation, d_o_b, gender, marital_status, email]
    details = []

    if not f_name.isalpha():
        print('wrong firstname')
        continue
    elif not l_name.isalpha():
        print('wrong lastname')
        continue
    elif not m_name.isalpha():
        print('wrong middlename')
        continue
    elif not age.isalnum():
        print('wrong age format')
        continue
    elif not occupation.isalpha():
        print('wrong occupation format')
        continue
    elif d_o_b.isalpha():
        print('wrong dob format')
        continue
    # elif gender != 'M' or gender != "F":
    #     print("wrong gender format")
    #     continue
    elif not marital_status.isalpha():
        print('wrong marital status')
        continue
    elif "@" not in email and "." not in email:
        print('wrong email format')
        continue
    else:
        details.append((f_name, l_name, m_name, age, occupation, d_o_b, gender, marital_status, email))
    break

with open("census.csv", 'w') as x:
    head_king = ["firstname", 'lastname', 'middle-name', 'age', 'occupation', "Date-of-birth", "gender",
                 'marital status', 'email']
    yu = csv.DictWriter(x, fieldnames=head_king)
    yu.writeheader()
    yu.writerow({
        "firstname": f_name,
        "lastname": l_name,
        "middle-name": m_name,
        "occupation": occupation,
        "age": age,
        "Date-of-birth": d_o_b,
        "gender": gender,
        'marital status': marital_status,
        'email': email
    })

with open("census.csv", "r") as q:
    hand = csv.DictReader(q)

    for rows in hand:
        print()


def search():
    global rows

    print("kindly provide the required details of the person you want to search for")
    time.sleep(2.2)
    f_n = input("kindly input the firstname\n")
    m_n = input("kindly input the middlename\n")
    l_n = input("kindly input the lastname\n")
    e_mail = input("kindly input the e_mail\n")

    for k, v in enumerate(rows):
        for f_n in rows:
            print(f" # {k}bears the name, {f_n},here are his details,{v}")
        for m_n in rows:
            print(f" # {k}bears the name, {m_n},here are his details,{v}")
        for l_n in rows:
            print(f" # {k}bears the name, {l_n},here are his details,{v}")
        for e_mail in rows:
            print(f" # {k} possess the e-mail, {e_mail},here are his details,{v}")

