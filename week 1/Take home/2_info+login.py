print("Kindly provide the required details")
f_name = str(input("input your firstname "))
l_name = str(input("input your lastname "))
u_name = str(input("Provide preferred username "))
p_word = str(input("provide a strong password "))

username = u_name
password = p_word


print("kindly provide your log-in details")

user = str(input('input your username '))
pword = str(input('input your password '))

if username == user and password == pword:
    print('login successful')
elif username != user or password != pword:
    print("Wrong password or username")
else:
    print("Wrong username and password")