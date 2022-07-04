import math
x = int(input("Define X "))
ex = 0
result = 1

while ex < (x + 1):
    ex_list = list(range(1 , ex + 1))
    ex_rev = list(reversed(ex_list))
    ex_factorial = math.prod(ex_rev)
    result *= (x ** ex) /ex_factorial
    ex += 1



    print(result)




# CONVERT FLOAT TO LIST, MAKE A LIST OF THE FLOATS,sum it up using math.fsum
