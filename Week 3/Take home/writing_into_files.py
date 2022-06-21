import shelve
import sys

u_name = input('kindly input a unique username \n')
f_name = input("kindly input your firstname \n")
l_name = input("kindly input your lastname \n")

while True:
    p_word = input("input a unique password \n")
    p_word_confirm = input("re_type your password \n")

    if p_word == p_word_confirm:
        details = {}

        details['username'] = u_name
        details['firstname'] = f_name
        details['lastname'] = l_name
        details['password'] = p_word
        details['password confirmation'] = p_word_confirm

        print(details)

        file = shelve.open(u_name)
        file['info'] = details
        file.close()

        x = shelve.open(u_name, 'r')
        print(list(x.values()))
        sys.exit()

    else:
        print('the password and the password confirmation does not match....kindly re-check')
        continue
