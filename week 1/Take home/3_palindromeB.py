drome = int(input("hello, Kindly fill in FIVE DIGITS !"))

palin = drome
y = 0

while palin > 0:
    y = y * 10 + palin % 10
    palin = palin // 10
print(y)

if drome == y and len(str(drome)) == 5:
    print(f"{drome} is a palindrome.")
elif drome == y and len(str(drome)) != 5:
    print(f'{drome} is a palindrome,but it does not conform to the instruction')
else:
    print('this is very wrong')


