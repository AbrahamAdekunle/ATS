import sys

u_name = input('kindly input a unique username \n')
f_name = input("kindly input your firstname \n")
l_name = input("kindly input your lastname \n")

while True:
    p_word = input("input a unique password \n")
    p_word_confirm = input("re_type your password \n")

    if p_word == p_word_confirm:
        file_name = f"{u_name}.txt"
        with open(file_name,"w") as x:
            x.write(f"{u_name},{f_name}, {l_name}, {p_word}")
            sys.exit()


    else:
        print("wrong password")
