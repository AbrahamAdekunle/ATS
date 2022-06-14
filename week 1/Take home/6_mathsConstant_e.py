import math
fact= int(input("Kindly input the number whose factorial, youll like to use "))

e = 0
while e < (fact + 1):
     e_list = list(range(1,e + 1))
     e_list_rev = list(reversed(e_list))
     factorial = math.prod (e_list_rev)
     result = 1 / factorial
     e += 1



     # print(result)
     print(result)

     #CONVERT FLOAT TO LIST, MAKE A LIST OF THE FLOATS,sum it up using math.fsum

