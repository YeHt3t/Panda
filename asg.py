def rate():
    while True:
        rate = float(input("Please give a rating out of 5: "))
        if rate > 5 :
            print("Invalid rating: Rating should be between 0 and 5")
        elif rate < 0 :
            print("You dislike it that much? Please enter a rating between 0 and 5")
        else:
            if rate > 3 :
                print("I'm happy you enjoyed")
            else:
                print("I apoligize you disliked it, please give some feedback")
                input("Feedback: ")
                print("Thank you for the feedback")
            break

