import random

val_list = list(range(1, 100))
rand_dict = {}

i = 0
while i < 20:
    r = random.choice(val_list)
    rand_dict[str(r)] = r
    i += 1
print(rand_dict)
value = [x for x in rand_dict.values()]

value.sort()

duplicate = [value[x] for x in range(len(value) - 1) if value[x] == value[x + 1]]
print(f"The amount of duplicate in the values are , {len(duplicate)}")


"""ANOTHER METHOD"""
v_set = set(value)

if len(v_set) == len(value):
    print("There are no duplicates")
else:
    print(f"there are {len(value) - len(v_set)} duplicates")
