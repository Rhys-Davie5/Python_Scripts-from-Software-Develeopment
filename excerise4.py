import random

# ----------------------------------------------------------------------------------------------------------------------
from typing import Any

count = 0
countdown = 6
Countdown1 = 6
def userguess():
    global count
    global countdown
    global Countdown1
    count=count+1
    countdown=countdown-1
    Countdown1=Countdown1+0

    userboard1 = random.randint(0, 10)
    userboard2 = random.randint(0, 10)

    print(userboard1)
    print(userboard2)

# ----------------------------------------------------------------------------------------------------------------------

    userguess100 = int(input("Please enter guess 1: "))
    while userguess100 > 10:
        print("that number is too big, try a smaller number")
        userguess100 = int(input("Please enter guess 1: "))
    while userguess100 < 0:
        print("that number is too small, try a bigger number")
        userguess100 = int(input("Please enter guess 1: "))
    userguess200 = int(input("Please enter guess 2: "))
    while userguess200 > 10:
        print("that number is too big, try a smaller number")
        userguess100 = int(input("Please enter guess 2: "))
    while userguess200 < 0:
        print("that number is too small, try a bigger number")
        userguess100 = int(input("Please enter guess 2: "))

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]

    useritem2 = (useritem[userguess100])
    useritem3 = (useritem[userguess200])

# ----------------------------------------------------------------------------------------------------------------------

    if userboard1 == userguess100 and userboard2 == userguess200:
        print("Both of them are a match, the first pair", userguess100, "was a", useritem2, "and the second pair", userguess200, "was a", useritem3)
        print("you have",countdown-1,"pairs left")

    else:
        print("Sorry that was not a match, the first pair", userguess100,"was a",useritem2, "and the second pair", userguess200, "was a", useritem3)
        print("you have", Countdown1, "pairs left")

    if countdown == 0:
        print("well done, you got them all. you did it in",count,"turns")
        exit()

    print("you've had", count, "turn(s) so far")
    print()

    repeat=userguess()
    print(repeat)
# -----------------------------------------------------------------------------------------------------------------------

print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")
userboard = "0 1 2 3 4 5 6 7 8 9 10"
print(userboard)
print("???????????")

userguess()

