import string

a_c_l = string.ascii_lowercase
vowels = ["a",'e','i','o','u']


a_c_set = set(a_c_l)
v_set = set (vowels)

a_c_set.update(v_set)
# print(a_c_set)
x = ",".join(a_c_set)
print(x)


