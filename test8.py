answer = 8
guess = int(input("Guess a number beween 1 ad 10 : "))
if guess > answer: 
    print("try smaller")
elif guess < answer: 
    print("try bigger")
elif guess == answer:
    print("bingo")
else:
    print("Invalid input, try again.")