import random

numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

choice = random.choice(numero)

for x in range(5,0,-1):
    number = int(input('Pick a number ?\n'))
    if number > choice :
        print(f" WRONG! your guess is greater than the choice...you have {x-1} tries left")
    elif number < choice :
        print(f"WRONG! your guess is lesser than the choice...you have {x - 1} tries left")
    elif number == choice:
        print("Correct, you guessed right")
        break
print(f"{choice}, is the correct answer....")

