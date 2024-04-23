import random
coin = random.randint(1,2)

choice = int(input("Enter your choice (head for 1/tail for 2) : "))

if choice == 1 and coin == 1:
    print("It's Head, You win")
elif choice ==  2 and coin == 1:
    print("It's Head, You lose")
elif choice == 2 and coin == 2:
    print("It's Tails, You win")
elif choice == 1 and coin == 2:
    print("It's Tails, You lose")
else:
    print("invalid answer")