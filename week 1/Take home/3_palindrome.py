p_drome = str(input("hello, Kindly fill in FIVE DIGITS !"))
drome_p = p_drome[::-1]

if p_drome == drome_p and len(p_drome) == 5 :
    print (f"{p_drome} is a palindrome.")
elif p_drome ==drome_p and len(p_drome) != 5:
    print(f'{p_drome} is a palindrome,but it does not conform to the instruction')
else:
    print('this is very wrong')
