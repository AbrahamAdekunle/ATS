import random
import string


def username_generator():
    f_name = list(input("type your first name \n"))
    m_name = list(input("type your middle name \n"))
    l_name = list(input("type your last name \n"))
    numero = string.digits

    username = f_name[0:2] + m_name[1:3] + l_name[0:2] + random.sample(numero, 3)
    return "".join(username).lower()


print(username_generator())
