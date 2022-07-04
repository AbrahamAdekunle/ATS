numero_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    1000: 'one thousand'
}


def number_2_words(numero: int) -> str:
    unit = numero % 10
    tens = ((numero % 100) // 10) * 10
    hundred = numero // 100 % 10
    thousand = numero // 1000

    if numero in numero_dict:
        return f" {numero_dict[numero]}"

    elif 20 < numero <= 99:
        return f" {numero_dict[tens]}  - {numero_dict[unit]}"

    elif 100 < numero <=999 and numero % 10 == 0:
        return f" {numero_dict[hundred]} hundred"

    elif 100 < numero <= 999:
        return f" {numero_dict[hundred]} hundred and {number_2_words(numero % 100)}"

    elif numero > 999:
        return f" {numero_dict[thousand]} thousand and {number_2_words(numero % 1000)}"


number = int(input("Type the number you would like to convert \n"))
print(number_2_words(number).title())





