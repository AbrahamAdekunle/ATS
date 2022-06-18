numero_dict = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "nineteen",
    '20': "twenty",
    '30': "thirty",
    '40': "fourty",
    '50': "fifty",
    '60': "sixty",
    '70': "seventy",
    '80': "eighty",
    '90': "ninety"
}


def tens():
    numero_x = int(number)

    tens, unit = divmod(numero_x, 10)

    tenth = str(tens)
    unith = str(unit)

    return f" {numero_dict[tenth + '0']} - {numero_dict[unith]}"


def hundred():
    numero_x = int(number)

    hundreed, tens = divmod(numero_x, 100)
    unit = tens % 10

    hundreth = str(hundreed)
    tenth = str(tens)
    unith = str(unit)

    if number[1] == "0" and number[2] == "0":
        return f" {numero_dict[hundreth]} hundred"
    elif number[2] == "0":
        return f"{numero_dict[hundreth]} hundred and {numero_dict[((tenth[0]) + '0')]}"
    elif number[1] == "0":
        return f"{numero_dict[hundreth]} hundred and {numero_dict[unith]}"
    elif number[1] == "1":
        return f"{numero_dict[hundreth]} hundred and {numero_dict[tenth]}"
    else:
        return f" {numero_dict[hundreth]} hundred and {numero_dict[((tenth[0]) + '0')]} - {numero_dict[unith]}"


def thousand():
    numero_x = int(number)

    thousandth, pseudo_h = divmod(numero_x, 1000)

    hundred, pseudo_t = divmod(pseudo_h, 100)

    tenth, unit = divmod(pseudo_t, 10)

    s_thou = str(thousandth)
    s_hund = str(hundred)
    s_tenth = str(tenth)
    s_pseu = str(pseudo_h)
    if number[1] == '0' and number[2] == '0' and number[3] == '0':
        return f"{numero_dict[s_thou]} thousand"
    elif number[2] == '0' and number[3] == '0':
        return f'{numero_dict[s_thou]} thousand, {numero_dict[s_hund]} hundred'
    elif number[1] == '0' and number[2] == '0':
        return f'{numero_dict[s_thou]} thousand and {numero_dict[(number[3])]}'
    elif number[1] == '0':
        return f' {numero_dict[s_thou]} thousand and {numero_dict[s_pseu]}'
    elif number[3] == '0':
        return f" {numero_dict[s_thou]} thousand, {numero_dict[s_hund]} hundred and {numero_dict[s_tenth + '0']}"
    else:
        return f" {numero_dict[s_thou]} thousand , {numero_dict[s_hund]} hundred and {numero_dict[s_tenth + '0']} - {numero_dict[number[3]]}"


number = str(input("Type the number you would like to convert  "))
if len(number) == 1:
    print(numero_dict[number])
elif len(number) == 2 and (number[0] == '1' or number[1] == '0'):
    print(numero_dict[number])
elif len(number) == 2 and number[0] != '1' and number[1] != '2':
    print(tens())
elif len(number) == 3:
    print(hundred())
elif len(number) == 4:
    print(thousand())
elif len(number) == 5 and number[1] == '0' and number[2] == '0' and number[3] == '0' and number[4] == '0':
    print(f" {numero_dict[(number[0] + '0')]} thousand ")
