import math
binary_int = int(input("Kindly input a binary integer (containing only 0 and 1) "))
bint_length = len(str((binary_int)))
power_of_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

p_bint = binary_int


i = 0
last_digit = 0

while i < bint_length:
    last_digit = last_digit * 10 + binary_int % 10
    i_val = last_digit * power_of_two[i]
    p_bint = p_bint // 2
    i +=1


bint_list = list(str(i_val))
# print(bint_list)

result = math.fsum(int(bint_list))

print (f" the decimal equivalent of {binary_int} is {result}")


# binary_int_list = list(str(binary_int))
# rev_binary_int_list = list(reversed(binary_int_list))
# tup_rev = tuple(rev_binary_int_list)

# def addnums (*args):
#     x = 0
#     for items in args:
#         x += items
#     return(x)






# i = binary_int
# while 1 > 0:
#     product = tup_rev[]
#



