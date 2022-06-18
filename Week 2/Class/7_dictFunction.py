import math

backend = {
    "back_1": {
        "firstname": "abraham",
        "lastname": "adekunle",
        "attendance": 12,
        "day of birth": 13,
        "month of birth": "january",
        "height": 180,
        "weight": 75,
        "age": 25
    },

    "back_2": {
        "firstname": "yussuff",
        "lastname": "oyedele",
        "attendance": 10,
        "day of birth": 21,
        "month of birth": "june",
        "height": 130,
        "weight": 65,
        "age": 28
    },

    "back_3": {
        "firstname": "awwal",
        "lastname": "adeleke",
        "attendance": 9,
        "day of birth": 4,
        "month of birth": "april",
        "height": 240,
        "weight": 78,
        "age": 27
    },

    "back_4": {
        "firstname": "adebusola",
        "lastname": "adeyeye",
        "attendance": 12,
        "day of birth": 17,
        "month of birth": "may",
        "height": 200,
        "weight": 98,
        "age": 29
    },

    "back_5": {
        "firstname": "bashir",
        "lastname": "balogun",
        "attendance": 8,
        "day of birth": 13,
        "month of birth": "march",
        "height": 170,
        "weight": 72,
        "age": 24
    },

    "back_6": {
        "firstname": "abdullahi",
        "lastname": "salaam",
        "attendance": 9,
        "day of birth": 30,
        "month of birth": "march",
        "height": 180,
        "weight": 75,
        "age": 27
    },

    "back_7": {
        "firstname": "faith",
        "lastname": "adeosun",
        "attendance": 11,
        "day of birth": 25,
        "month of birth": "september",
        "height": 15,
        "weight": 67,
        "age": 28
    },

    "back_8": {
        "firstname": "ahmad",
        "lastname": "sharaufdeen",
        "attendance": 10,
        "day of birth": 13,
        "month of birth": "november",
        "height": 189,
        "weight": 79,
        "age": 34
    },

    "back_9": {
        "firstname": "lukman",
        "lastname": "abisoye",
        "attendance": 11,
        "day of birth": 21,
        "month of birth": "december",
        "height": 190,
        "weight": 87,
        "age": 28
    },

    "back_10": {
        "firstname": "Toluwanimi",
        "lastname": "ogunbiyi",
        "attendance": 11,
        "day of birth": 24,
        "month of birth": "november",
        "height": 180,
        "weight": 75,
        "age": 24
    },

    "back_11": {
        "firstname": "Abdulwalii",
        "lastname": "Tajudeen",
        "attendance": 7,
        "day of birth": 17,
        "month of birth": "november",
        "height": 198,
        "weight": 75,
        "age": 45
    }
}


# return number of people
def population(list):
    return (len(list))


# print(population(backend))

# Remove Profile
def remove(data, firstname):
    for x in data:
        if data[x]["firstname"] == firstname:
            del data[x]
            return data


# Attendance
def attendance(data, firstname, num):
    z = 0
    for x in data:
        if data[x]["firstname"] == firstname:
            z = z + (data[x]["attendance"]) + num
            data[x]["attendance"] = z
            data[x]["attendance"] += num
            return data


# update name
def update_name(data, firstname, lastname, n_first, n_last):
    for x in data:
        if data[x]['firstname'] == firstname and data[x]['lastname'] == lastname:
            data[x]['firstname'] = n_first
            data[x]['lastname'] = n_last

        return data


# BMI
def bmi(data, firstname):
    body = 0
    for x in data:
        if data[x]['firstname'] == firstname:
            body += data[x]['weight'] / ((data[x]['height'] / 100) ** 2)
        return body


# max num
def max_number(data):
    highest_number = 0
    age = []
    for x in data:

        if True:
            age.append(data[x]['age'])

    highest_number += 0
    for numero in age:
        if numero > highest_number:
            highest_number = numero

    return highest_number


# average
def average(data):
    result = 0
    age = []
    for x in data:
        if True:
            age.append(data[x]["age"])

    result += math.fsum(age) / len(age)
    return result


# minimum
def minimum(data):
    age = []
    for x in data:
        age.append(data[x]["age"])

    lowest_number = age[0]
    for numero in age:
        if numero < lowest_number:
            lowest_number = numero

    return lowest_number


# fullname in titlecase
def titlecase(data, firstname):
    for x in data:
        if data[x]['firstname'] == firstname:
            return (data[x]["firstname"]).title() + ' ' + (data[x]['lastname']).title()


def title(data):
    full_name = []
    for x in data:
        if True:
            full_name.append((data[x]["firstname"]).title() + ' ' + (data[x]['lastname']).title())
    return full_name


# birthmonth
def birth_month(data, firstname):
    for x in data:
        if data[x]['firstname'] == firstname:
            return data[x]['month of birth']


# initials
def initials(data):
    init = []
    for x in data:
        if True:
            a_in = (data[x]["firstname"].upper())[0]
            l_in = (data[x]["lastname"].upper())[0]
            result = a_in + "." + l_in
            init.append(result)

    return init


# add profile
def add_profiles(data):
    n_data = {}
    firstname = input("what is your firstname ? ")
    lastname = input("what is your lastname  ?")
    atten_dance = int(input("input the number of times you were present"))
    day_ob = int(input("what is your DAY of birth ?"))
    month_ob = input("what is your Month of birth ?")
    h_ight = int(input("what is your height ? "))
    w_ight = int(input("what is your weight ? "))
    age = int(input("what is your age ? "))

    n_data['firstname'] = firstname
    n_data['lastname'] = lastname
    n_data['attendance'] = atten_dance
    n_data['day of birth'] = day_ob
    n_data['month of birth'] = month_ob
    n_data['height'] = h_ight
    n_data['weight'] = w_ight
    n_data['age'] = age

    data.update(n_data)

    return data


# print(add_profiles(backend))
# print(backend)

# group profile
def g_profile(data):
    first_quarter = []
    second_quarter = []
    third_quarter = []
    fourth_quarter = []
    for x in data:
        if data[x]['month of birth'] == 'january' or data[x]['month of birth'] == 'february' or data[x][
            'month of birth'] == 'march':
            first_quarter.append(data[x])
        elif data[x]['month of birth'] == 'may' or data[x]['month of birth'] == 'june' or data[x][
            'month of birth'] == 'april':
            second_quarter.append(data[x])
        elif data[x]['month of birth'] == 'july' or data[x]['month of birth'] == 'august' or data[x][
            'month of birth'] == 'september':
            third_quarter.append(data[x])
        elif data[x]['month of birth'] == 'october' or data[x]['month of birth'] == 'november' or data[x][
            'month of birth'] == 'december':
            fourth_quarter.append(data[x])

        groups = first_quarter + second_quarter + third_quarter + fourth_quarter
    return groups


print(g_profile(backend))


# birthyear
def birthyear(data, firstname):
    for x in data:
        if data[x]["firstname"] == firstname:
            birth_y = 2022 - (data[x]["age"])

            return birth_y
