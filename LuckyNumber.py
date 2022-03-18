import random

print("Do you want to play Jackpot? yes/no?")
print()
print("1. Yes")
print("2. No")

userChoice1 = int(input())

if userChoice1 == 1:
    print("Ok lets get started")

else:
    userChoice1 == 2
    print("Ok bye")
    exit()

myNumber = random.randint(1, 2)
luckyNumber = random.randint(1, 2)

print("And your lucky number is... ", luckyNumber)

if myNumber == luckyNumber:

    print("Congrats, you just won the lottery!")

else:
    print("Sorry, you aren't a winner the winning number is", myNumber)

while True:
    print("Do you want to play Jackpot? yes/no?")
    print()
    print("1. Yes")
    print("2. No")

    userChoice1 = int(input())

    if userChoice1 == 1:
        print("Ok lets get started")

    else:
        userChoice1 == 2
        print("Ok bye")
        exit()

    myNumber = random.randint(1, 2)
    luckyNumber = random.randint(1, 2)

    print("And your lucky number is... ", luckyNumber)

    if myNumber == luckyNumber:

        print("Congrats, you just won the lottery!")

    else:
        print("Sorry, you aren't a winner the winning number is", myNumber)



