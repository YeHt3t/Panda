#a practice file for a "calculator" to add subtract divide or multiply 2 numbers of any kind
from asg import rate

name = input("Enter Username: ")
print("Hello", name)
print("Welcome to calculate any 2 numbers ^-^")
print("Here you can calculate 2 numbers of any kind be it and integer or decimal")
print("Let's Begin!")
first = float(input ("Enter first number: "))
second = float(input("Enter how much you would like to add, subtract, multiply or divide: "))
while True:
    third = input("would you like to add, subtract, multiply or divide: ")
    if third == "add":
        print("answer is: ", float(first + second))
        break
    elif third == "subtract":
        print("answer is: ", float(first - second))
        break
    elif third == "divide":
        print("answer is: ", float(first / second))
        break
    elif third == "multiply":
        print("answer is: ", float(first * second))
        break
    else: 
        print("Invalid; please enter add, subtract, divide or multiply")

rate()