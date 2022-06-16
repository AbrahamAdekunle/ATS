numero_dict={
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


# print(numero_dict[20])
def numbers_to_words(name:str)-> str:
    words =[]
    if len(name) == 1:                       #unit
        words.append(numero_dict[name])
    elif len(name) ==2 and name[1] == '0':    #tens
           words.append(numero_dict[name])
    elif len(name) == 2 and name[0] == '1' :
         words.append(numero_dict[name])
    elif len(name) == 2 and name[0] == '2':
        words.insert(0,'twenty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '3':
        words.insert(0, 'thirty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '4':
        words.insert(0, 'forty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '5':
        words.insert(0, 'fifty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '6':
        words.insert(0, 'sixty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '7':
        words.insert(0, 'seventy-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '8':
        words.insert(0, 'eighty-')
        words.insert(1, (numero_dict[name[1]]))
    elif len(name) == 2 and name[0] == '9':
        words.insert(0, 'ninety-')
        words.insert(1, (numero_dict[name[1]]))

    elif len(name) == 3 and name[1] == '0' and name[2] == '0':      #hundred
        words.append((numero_dict[name[0]]) + " " + "hundred")
    elif len(name) == 3 and name[0] == '1' and name[1] == '0':
        words.insert(0,"One hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '1':
        words.insert(0, "One hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[2] == '0':
        words.insert(0, "One hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '2':
        words.insert(0, "One hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '3':
        words.insert(0, "One hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '4':
        words.insert(0, "One hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '5':
        words.insert(0, "One hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '6':
        words.insert(0, "One hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '7':
        words.insert(0, "One hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '8':
        words.insert(0, "One hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '1' and name[1] == '9':
        words.insert(0, "One hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '2' and name[1] == '0':
        words.insert(0, "two hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '1':
        words.insert(0, "two hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[2] == '0':
        words.insert(0, "two hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '2':
        words.insert(0, "two hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '3':
        words.insert(0, "two hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '4':
        words.insert(0, "two hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '5':
        words.insert(0, "two hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '6':
        words.insert(0, "two hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '7':
        words.insert(0, "two hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '8':
        words.insert(0, "two hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '2' and name[1] == '9':
        words.insert(0, "two hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '3' and name[1] == '0':
        words.insert(0, "three hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '1':
        words.insert(0, "three hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[2] == '0':
        words.insert(0, "three hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '2':
        words.insert(0, "three hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '3':
        words.insert(0, "three hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '4':
        words.insert(0, "three hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '5':
        words.insert(0, "three hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '6':
        words.insert(0, "three hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '7':
        words.insert(0, "three hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '8':
        words.insert(0, "three hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '3' and name[1] == '9':
        words.insert(0, "three hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '4' and name[1] == '0':
        words.insert(0, "four hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '1':
        words.insert(0, "four hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[2] == '0':
        words.insert(0, "four hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '2':
        words.insert(0, "four hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '3':
        words.insert(0, "four hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '4':
        words.insert(0, "four hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '5':
        words.insert(0, "four hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '6':
        words.insert(0, "four hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '7':
        words.insert(0, "four hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '8':
        words.insert(0, "four hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '4' and name[1] == '9':
        words.insert(0, "four hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '5' and name[1] == '0':
        words.insert(0, "five hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '1':
        words.insert(0, "five hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[2] == '0':
        words.insert(0, "five hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '2':
        words.insert(0, "five hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '3':
        words.insert(0, "five hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '4':
        words.insert(0, "five hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '5':
        words.insert(0, "five hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '6':
        words.insert(0, "five hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '7':
        words.insert(0, "five hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '8':
        words.insert(0, "five hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '5' and name[1] == '9':
        words.insert(0, "five hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '6' and name[1] == '0':
        words.insert(0, "six hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '1':
        words.insert(0, "six hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[2] == '0':
        words.insert(0, "six hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '2':
        words.insert(0, "six hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '3':
        words.insert(0, "six hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '4':
        words.insert(0, "six hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '5':
        words.insert(0, "six hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '6':
        words.insert(0, "six hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '7':
        words.insert(0, "six hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '8':
        words.insert(0, "six hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '6' and name[1] == '9':
        words.insert(0, "six hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))


    elif len(name) == 3 and name[0] == '7' and name[1] == '0':
        words.insert(0, "seven hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '1':
        words.insert(0, "seven hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[2] == '0':
        words.insert(0, "seven hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '2':
        words.insert(0, "seven hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '3':
        words.insert(0, "seven hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '4':
        words.insert(0, "seven hundred and forty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '5':
        words.insert(0, "seven hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '6':
        words.insert(0, "seven hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '7':
        words.insert(0, "seven hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '8':
        words.insert(0, "seven hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '7' and name[1] == '9':
        words.insert(0, "seven hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '8' and name[1] == '0':
        words.insert(0, "eight hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '1':
        words.insert(0, "eight hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[2] == '0':
        words.insert(0, "eight hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '2':
        words.insert(0, "eight hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '3':
        words.insert(0, "eight hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '4':
        words.insert(0, "eight hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '5':
        words.insert(0, "eight hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '6':
        words.insert(0, "eight hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '7':
        words.insert(0, "eight hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '8':
        words.insert(0, "eight hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '8' and name[1] == '9':
        words.insert(0, "eight hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))

    elif len(name) == 3 and name[0] == '9' and name[1] == '0':
        words.insert(0, "nine hundred and ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '1':
        words.insert(0, "nine hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[2] == '0':
        words.insert(0, "nine hundred and ")
        words.insert(1, (numero_dict[name[1] + name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '2':
        words.insert(0, "nine hundred and twenty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '3':
        words.insert(0, "nine hundred and thirty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '4':
        words.insert(0, "nine hundred and fourty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '5':
        words.insert(0, "nine hundred and fifty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '6':
        words.insert(0, "nine hundred and sixty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '7':
        words.insert(0, "nine hundred and seventy ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '8':
        words.insert(0, "nine hundred and eighty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 3 and name[0] == '9' and name[1] == '9':
        words.insert(0, "nine hundred and ninty ")
        words.insert(1, (numero_dict[name[2]]))
    elif len(name) == 4 and name[1] == '0' and name[2] =='0' and name[3] == '0':
        words.append((numero_dict[name[0]]) + " "+ "thousand")
    else:
        print("number is out of range")



    return "".join(words).title()


print(numbers_to_words("1000"))