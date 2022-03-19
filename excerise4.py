import random

def userGuess():
    userGuess1 = input("Please enter your first guess: ")
    userGuess2 = input("Please enter your second guess: ")

    while userGuess1 == userBoard2:
        print("its a match")
    print()

    while userGuess2 == userBoard3:
        print("its a match")
    print("Both of them are a match, the first pair was",userBoard2, "and the second pair was", userBoard3)

    if userGuess1 and userGuess2 != userBoard2 and userBoard3:
        print("Not a match, the first pair was",userBoard2, "and the second pair was", userBoard3)

#-----------------------------------------------------------------------------------------------------------------------

print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")

userBoard = "0 1 2 3 4 5 6 7 8 9 10"
print(userBoard)
print("???????????")

userBoard2 = random.randint(0, 10)
userBoard3 = random.randint(0, 10)

print(userBoard2)
print(userBoard3)

userGuess()






