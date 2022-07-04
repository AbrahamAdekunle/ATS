import math
fact = int(input("kindly input a number "))


# def multiply (*z):
#     x = 1
#     for chars in z:
#         x *= chars
#         return x
if fact > 0:
    f_char = list(range(1,fact + 1 ))
# print(f_char)

    f_char_rev = list(reversed(f_char))
# print(f_char_rev)

# f_char_tup = tuple(f_char_rev)
# print(f_char_tup)

# print(multiply (f_char_rev))

    result = math.prod(f_char_rev)
    print(result)

else:
    print('input number greater than zero')




#LIMIT IS 8 CHARACTERS
