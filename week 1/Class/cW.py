
# number_list = [1,2,3,4,5]
# number_string = 'vagrant'
# number_set ={ 1,2,3,4,5,6,7,8,9}
# number_tuple = (1,2,3,4,5,6)
# number_dict = {'q':1,'e':1,'a':3}
#
#
#
# print(list (number_tuple) + list (number_set))

# i=0
# while i < len(number_list):
#     print(number_list[i])
#     i+=1


# numbers = [1,2,3,4,5,6,7,8,9]
#
# for item in numbers:
# #     if item % 2 == 0:
# #         print (item)
# #
#
#
# # i = 0
# while i< len(numbers):
#     if item % 2 == 0:
#         print(item)
#             i+=1

# secret_number = 39
#
#
# guess_count = 0
#
# while guess_count <= 3:
#     guess = input("what is your number ? ")
#     guess_count+=1
#     if guess_count == secret_number:
#         name = input("what is your name ? ")
#         print(f"you got it {name}")
#         break
#     else:
#         na_me = input("what is your name ? ")
#         print(f"you are a loser, {na_me}")



# def multiply (a,b):
#     print (a * b)
#
# print(multiply (9,5))



# def square (a):
#     return(a ** 2 )
#
# square(3)


# print("hello")
# for x in range(0,50,4):
#     print(f"hello {x}")

#
# total = 0
#
# for x in range (101):
#  total += x
#  print(total)


# ome = 123345664
## print(len(drome))



# def funcdt (kwargs = {'x':2, 'y':3}):
#
# def func (x,y):
#     print( x + y)
#
# func (2,3)
#
# joke_lisy = [3, 4, 5, 7, 8, 9]
#
#
# def numbe (*toy):
#     x = 1
#     for items in toy:
#         x += sum(items)
#         return x
#
# print(numbe(joke_lisy))




# p_check = int(input("Inout the number which you will like to confirm if it is a prime number or not"))
#
#
#
# if p_check > 1:
#      for i in range (2,p_check):
#          if (p_check % i) == 0 :
#              print (f" {p_check} is not a prime number , it is divisible by {i}")
#              break
#
#
#          else:
#              print(f'{p_check} is a prime number')
#              break
#
# else:
#     print(f" {p_check} is not a prime number")

# import math
# fact = int(input("what is the number , which you wil like to get its factorial :  "))
#
#
# f_list = list(range(1,fact+1))
#
# f_rev = list(reversed(f_list))
#
# answer = math.prod(f_rev)
#
# print(answer)




#check prime number for an interval

lower = int(input("input the lower limit : "))
upper = int(input("input the upper limit : "))


for numb in range (lower, upper + 1):

    for items in range (2 , numb):
        if (numb % items) == 0:
            break
        else:
            print(numb)
            break