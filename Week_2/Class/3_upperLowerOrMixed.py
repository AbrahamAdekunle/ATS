import string

a_c_l = string.ascii_lowercase
a_c_u =  string.ascii_uppercase
word = str(input("input the word you want to check"))


def check (data:str):


d_list = list(data)

d_list.remove(" ")
aclu = a_c_l + a_c_u

upper = []
lower = []
up_low = []

    for items in d_list:
        if items in a_c_l:
            upper.append(items)
            if len(upper) == len (d_list):
                print(f'{data} is in upper case')
                break

        elif items in a_c_u:
            lower.append(items)
            if len(lower) == len(d_list):
                print(f'{data} is in lower case')
                break

        elif items in aclu:
            up_low.append(items)
            if len(up_low) == len(d_list):
                print(f'{data} is in mixed case')
                break



