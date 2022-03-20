import random

# ----------------------------------------------------------------------------------------------------------------------
turns = 0
Pairs = 0
countdown = 6
Same = 6

def userguess():
    global turns # count how many times ive looped
    global countdown # take away completed pairs
    global Same # number stays the same
    global Pairs
    turns=turns+1  # adds a 1
    countdown=countdown-1  # takes away 1
    Same=Same+0  # stays the same
    Pairs=Pairs+1

    userboard1 = random.randint(0, 10)
    userboard2 = random.randint(0, 10)

    print(userboard1)
    print(userboard2)

    #print(userboard1)
    #print(userboard2)

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



# ----------------------------------------------------------------------------------------------------------------------

    if Pairs == 6:
        print("well done, you got them all. you did it in", turns, "turns")
        print("you have succesfully obtained", Pairs, "pairs, congratulations!")
        exit()

    if userboard1 == userguess100 and userboard2 == userguess200:
        print("Both of them are a match, the first pair", userguess100, "was a", useritem2, "and the second pair", userguess200, "was a", useritem3)
        print("you now have",Pairs,"pair(s)")
        print("you have", turns, "turn(s) so far")

    else:
        print("Sorry that was not a match")
        print("You have used", turns, "turn(s) so far")

# ----------------------------------------------------------------------------------------------------------------------
    print()
    repeat=userguess()
    print(repeat)
# ----------------------------------------------------------------------------------------------------------------------
print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")
userboard = "0 1 2 3 4 5 6 7 8 9 10"
print(userboard)
print("? ? ? ? ? ? ? ? ? ? ?")
userguess()