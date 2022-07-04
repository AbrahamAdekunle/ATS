numb_list = [1, 2, 3, 4, 5]
n_list = [6,7,8,9,10]

new_list = numb_list + n_list
print(new_list)

even_number = []

for x in new_list:
    if x % 2 == 0:
        even_number.append(x)
    else:
        new_list.remove(x)

print(even_number)
print(x)