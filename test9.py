answer= input("""

        Enter the weather
        (rainy, sunny or windy)

""")
if answer == "rainy":
    print("Bring an umbrella")
elif answer == "sunny":
    print("Stay hydrated and use sun-cream")
elif answer == "windy":
    print("Be careful of flying objects")
else:
    print("Invalid, please enter rainy, sunny or windy")