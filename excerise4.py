import random

count = 0
def userguess():
    global count
    count=count+1

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
    userboard1 = random.randint(0, 10)
    userboard2 = random.randint(0, 10)

    userguess100 = int(input("Please enter guess 1: "))
    userguess200 = int(input("Please enter guess 2: "))

    if userboard1 == userguess100 and userboard2 == userguess200:
        print("Both of them are a match, the first pair was a", userboard1, "and the second pair was", userboard2)
    else:
        print("Sorry that was not a match, the first pair was a", userboard1, "and the second pair was", userboard2)

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

