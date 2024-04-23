username = input("Hi, Welcome to converters, Please enter your name: ")
print("Hello, ", username, ". Here you can convert units. eg; CM to FT")
while True:
    unit = input("Please state which unit you would like to convert. farenheit, celsius, : ")
    if unit == "farenheit":
        print("farenheit to celsius chosen")
        num = float(input("Please state the number you would like to convert: "))
        print("Answer is", ((num - 32) * 5/9))
        again = input("Would you like to try again? ")
        if again == "no":
           break
        if again == "yes":
           print("Okay")
    elif unit == "celsius":
        print("celsius to farenheit chosen")
        num = float(input("Please state the number you would like to convert: "))
        print("Answer is", ((num * 9/5) + 32))
        again = input("Would you like to try again? ")
        if again == "no":
           print("Okay")
           break
        if again == "yes":
           print("Okay")
    elif unit == "centimeter":
        print("celsius to farenheit chosen")
        num = float(input("Please state the number you would like to convert: "))
        print("Answer is", ((num * 9/5) + 32))
        again = input("Would you like to try again? ")
        if again == "no":
           print("Okay")
           break
        if again == "yes":
           print("Okay")
    else:
        print("Invalid unit")