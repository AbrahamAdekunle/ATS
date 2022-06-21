import csv

# with open("first.csv", "r") as f:
#     handler = csv.reader(f)
#
#     for row in handler:
#         print(row)
#
# with open("first.csv", "a") as y:
#     hand = csv.writer(y)
#     hand.writerow(["firstname", "lastname", "username"])

with open("first.csv", "a") as z:
    header = [ "right", "left", "up", "down"]
    yu = csv.DictWriter(z, fieldnames=header)
    # yu.writerows()["right" : 'leg', "up":"head", "down":"femur", "left":"hand"])
    # print(list(yu))


