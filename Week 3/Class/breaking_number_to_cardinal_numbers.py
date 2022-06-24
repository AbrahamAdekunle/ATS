
def number_2_cardinal(number:int) -> str:
    numb_dict = {
        1: "st",
        2: "nd",
        3: "rd"
    }

    number_conv = number % 10
    if number == 11:
        return " 11th"
    elif number == 12:
        return '12th'
    elif number == 13:
        return '13th'
    elif number_conv == 1 and number < 100:
        return f" {number}{numb_dict[1]}"
    elif number_conv == 2 and number < 100:
        return f" {number}{numb_dict[2]}"
    elif number_conv == 3 and number < 100:
        return f" {number}{numb_dict[3]}"
    return f'{number}th'

print(number_2_cardinal(91))