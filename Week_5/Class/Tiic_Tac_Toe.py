import random
import sys


class TicTacToe:
    tic_tac_toe = [["tl", "tm", "tr"],
                   ["ml", "mm", "mr"],
                   ["bl", "bm", "br"]]

    possible_picks = [[0, 0], [0, 1], [0, 2],
                      [1, 0], [1, 1], [1, 2],
                      [2, 0], [2, 1], [2, 2]]

    checker = []

    def __init__(self):
        self.board = TicTacToe.tic_tac_toe

    def __repr__(self):
        return self.board

    def play_with_human(self):
        turn = "X"
        for x in range(9):
            while True:
                print(f" {turn}'s turn, DONT USE NEGATIVE INDEX")
                sub_1 = int(input("Input the first subscript of the position you'll like to play \n"))
                sub_2 = int(input("Input the second subscript of the position you'll like to play \n"))
                choice = [sub_1, sub_2]
                if choice in TicTacToe.possible_picks and choice not in TicTacToe.checker:
                    TicTacToe.checker.append(choice)
                    break
                else:
                    print(f"Error! Subscript combo invalid , enter another")
                    continue
            TicTacToe.tic_tac_toe[sub_1][sub_2] = turn
            print(TicTacToe.board())
            TicTacToe.confirmation()
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        return "This is a tie"

    def play_with_computer(self):
        turn = "X"
        for x in range(9):
            if turn == "X":
                while True:
                    print(f" {turn}'s turn, DONT USE NEGATIVE INDEX")
                    sub_1 = int(input("Input the first subscript of the position you'll like to play \n"))
                    sub_2 = int(input("Input the second subscript of the position you'll like to play \n"))
                    choice = [sub_1, sub_2]
                    if choice in TicTacToe.possible_picks and choice not in TicTacToe.checker:
                        TicTacToe.checker.append(choice)
                        break
                    else:
                        print(f"Error! Subscript combo invalid , enter another")
                        continue
                TicTacToe.tic_tac_toe[sub_1][sub_2] = turn
                print(TicTacToe.board())
                TicTacToe.confirmation()
            elif turn == "O":
                while True:
                    computer_move = [(random.randint(0, 2)), (random.randint(0, 2))]
                    if computer_move in TicTacToe.possible_picks and computer_move not in TicTacToe.checker:
                        TicTacToe.checker.append(computer_move)
                        break
                    else:
                        continue
                TicTacToe.tic_tac_toe[computer_move[0]][computer_move[1]] = turn
                print(TicTacToe.board())
                TicTacToe.confirmation()
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        return "This is a tie"

    @staticmethod
    def confirmation():
        if TicTacToe.tic_tac_toe[2][0] == "X" and TicTacToe.tic_tac_toe[2][1] == "X" and TicTacToe.tic_tac_toe[2][
            2] == "X":
            print("X wins via horizontal alignment of the bottom row")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][0] == "O" and TicTacToe.tic_tac_toe[2][1] == "O" and TicTacToe.tic_tac_toe[2][
            2] == "O":
            print("O wins via horizontal alignment of the bottom row")
            print("Thank you for gaming with us !")
            sys.exit()

        elif TicTacToe.tic_tac_toe[2][0] == "X" and TicTacToe.tic_tac_toe[1][0] == "X" and TicTacToe.tic_tac_toe[0][
            0] == "X":
            print("X wins via vertical alignment of the left column")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][0] == "O" and TicTacToe.tic_tac_toe[1][0] == "O" and TicTacToe.tic_tac_toe[0][
            0] == "O":
            print("O wins via vertical alignment of the left column")
            print("Thank you for gaming with us !")
            sys.exit()

        elif TicTacToe.tic_tac_toe[0][0] == "X" and TicTacToe.tic_tac_toe[0][1] == "X" and TicTacToe.tic_tac_toe[0][
            2] == "X":
            print("X wins via horizontal alignment of the top row")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[0][0] == "O" and TicTacToe.tic_tac_toe[0][1] == "O" and TicTacToe.tic_tac_toe[0][
            2] == "O":
            print("O wins via horizontal alignment of the top row")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][2] == "X" and TicTacToe.tic_tac_toe[1][2] == "X" and TicTacToe.tic_tac_toe[0][
            2] == "X":
            print("X wins via vertical alignment of the right column")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][2] == "O" and TicTacToe.tic_tac_toe[1][2] == "O" and TicTacToe.tic_tac_toe[0][
            2] == "O":
            print("X wins via vertical alignment of the right column")
            print("Thank you for gaming with us !")
            sys.exit()

        elif TicTacToe.tic_tac_toe[2][2] == "X" and TicTacToe.tic_tac_toe[1][1] == "X" and TicTacToe.tic_tac_toe[0][
            0] == "X":
            print("X wins via left - right diagonal alignment ")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][2] == "O" and TicTacToe.tic_tac_toe[1][1] == "O" and TicTacToe.tic_tac_toe[
            0][0] == "O":
            print("O wins via left -right diagonal alignment")
            print("Thank you for gaming with us !")
            sys.exit()

        elif TicTacToe.tic_tac_toe[2][0] == "X" and TicTacToe.tic_tac_toe[1][1] == "X" and TicTacToe.tic_tac_toe[0][
            2] == "X":
            print("x wins via right - left diagonal alignment ")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][0] == "O" and TicTacToe.tic_tac_toe[1][1] == "O" and TicTacToe.tic_tac_toe[0][
            2] == "O":
            print("O wins via right -left diagonal alignment")
            print("Thank you for gaming with us !")
            sys.exit()

        elif TicTacToe.tic_tac_toe[2][1] == "X" and TicTacToe.tic_tac_toe[1][1] == "X" and TicTacToe.tic_tac_toe[0][
            1] == "X":
            print("X wins via vertical alignment of the middle column")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[2][1] == "O" and TicTacToe.tic_tac_toe[1][1] == "O" and TicTacToe.tic_tac_toe[0][
            1] == "O":
            print("O wins via vertical alignment of the middle column")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[1][0] == "X" and TicTacToe.tic_tac_toe[1][1] == "X" and TicTacToe.tic_tac_toe[1][
            2] == "X":
            print("X wins via horizontal alignment of the middle row")
            print("Thank you for gaming with us !")
            sys.exit()
        elif TicTacToe.tic_tac_toe[1][0] == "O" and TicTacToe.tic_tac_toe[1][1] == "O" and TicTacToe.tic_tac_toe[1][
            2] == "O":
            print("O wins via horizontal alignment of the middle row")
            print("Thank you for gaming with us !")
            sys.exit()

    @staticmethod
    def board():
        print(f' {TicTacToe.tic_tac_toe[0][0]} | {TicTacToe.tic_tac_toe[0][1]} | {TicTacToe.tic_tac_toe[0][2]}  ')
        print("-----------")
        print(f' {TicTacToe.tic_tac_toe[1][0]} | {TicTacToe.tic_tac_toe[1][1]} | {TicTacToe.tic_tac_toe[1][2]}  ')
        print("-----------")
        print(f' {TicTacToe.tic_tac_toe[2][0]} | {TicTacToe.tic_tac_toe[2][1]} | {TicTacToe.tic_tac_toe[2][2]}  ')
        return "Tic-Tac-Toe"


TicTacToe().play_with_human()
# print(t)
