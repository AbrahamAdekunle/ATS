import string


a_c_l = string.ascii_lowercase
vowels = ["a",'e','i','o','u']

vow =[]

#1 list of first 10 elements
print(a_c_l[0:9])

#2 list of last 10 element
print(a_c_l[-10::])

#3 vowels
vow = []
for x in vowels:
    if x in a_c_l:
        # vow.append(x)
        print(x)

#4 for consonants
a_set = set(a_c_l)
v_set = set(vowels)

c_set = list(a_set.symmetric_difference(vowels))

print(c_set)