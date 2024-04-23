username = "Ye Htet"
pwd = "12345678"

user = input("Enter your username : ")
password = input("Enter Password : ")

if username == user and pwd == password == pwd:
    print("Welcome, ", user)
elif username == user and password != pwd:
    print("wrong password")
elif username != user or pwd != password:
    print("Wrong Username or password")
else:
    print("Something went wrong, Please try again")
