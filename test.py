while True : 
    Gender = input("Please enter your gender : ")
    if Gender == "male" or Gender == "Male" :
        print("Please proceed towards the right")
        break
    if Gender == "female" or Gender == "Female" :
        print("Please proceed towards the left")
        break
    if Gender == "disabled" or  Gender == "Disabled" :
        print("Please proceed straight ahead!")
        break
    else : 
        print("Gender not valaid, plese choose either male or female. Thank you!")