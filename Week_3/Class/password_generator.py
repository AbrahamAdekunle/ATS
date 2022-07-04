import random
import string


def password_generator():
    p_spec_char = string.punctuation
    p_numero = string.digits
    p_upper = string.ascii_uppercase
    p_lower = string.ascii_lowercase

    pass_test = p_lower + p_upper + p_numero + p_spec_char
    password = random.sample(pass_test, 20)

    return "".join(password)


print(password_generator())