import random
import sys


def fetch_data():
    with open("8_letter _words.txt", 'r') as w:
        return list(w)


def hang():
    data = fetch_data()
    rand_choice = random.choice(data).strip()
    print(rand_choice)
    rand_copy = list(rand_choice)
    hidden = list("_" * (len(rand_choice)))
    print(f'Hint: {"".join(hidden)} , is the format of the word')

    # test = []
    for x in range(len(rand_choice) * 2, 0, -1):
        picked_letter = validate_picked_letter()
        if picked_letter in rand_copy:
            hidden[rand_copy.index(picked_letter)] = picked_letter
            rand_copy[rand_choice.index(picked_letter)] = "#"
            # rand_copy
            print(f"correct, {hidden}")
            if "".join(hidden) == rand_choice:
                print(f"Well done !, {rand_choice} is correct")
                return intro()
            continue

        print(f"{picked_letter} is not part of the word......you have {x - 1} tries left")
    print("You ran out of tries, Game over")
    return intro()


def validate_picked_letter():
    picked_letter = str(input('pick a letter \n'))
    if picked_letter.isalpha() and len(picked_letter) == 1:
        return picked_letter
    print("invalid format")
    return validate_picked_letter()


def intro():
    choice = input('HANGMAN.......to start press (1) , press any other key to exit \n')
    if choice == '1':
        return hang()
    print('Thank you')
    sys.exit()


print(intro())
