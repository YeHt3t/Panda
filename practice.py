#a practice file for a "calculator" to add subtract divide or multiply 2 numbers of any kind

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
while True:
    rate = float(input("Please give a rating out of 5: "))
    if rate > 5 :
        print("Invalid rating: Rating should be between 0 and 5")
    elif rate < 0 :
        print("Invalid rating: Rating should be between 0 and 5")
    else:
        if rate > 3 :
            print("I'm happy you enjoyed")
        else:
            print("I apoligize you disliked it, please give some feedback")
            input("Feedback: ")
        
            print("Thank you for the feedback")
        break
