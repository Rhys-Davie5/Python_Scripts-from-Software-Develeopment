import random

# ----------------------------------------------------------------------------------------------------------------------
turns = 0
SetPairs = 6
Pairs = 0
PairsN = 1

def userguess():
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
        userguess200 = int(input("Please enter guess 2: "))
    while userguess200 < 0:
        print("that number is too small, try a bigger number")
        userguess200 = int(input("Please enter guess 2: "))

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
    useritem2 = (useritem[userguess100]) # guess an animal for guess 1
    useritem3 = (useritem[userguess200]) # guess an animal for guess 1

    dog = 1
    cat = 1
    turtle = 1
    snake = 1
    hamster = 1
    lion = 1
    wolf = 1
    monkey = 1
    bird = 1
    dinosaur = 1
    dragon = 1

# ----------------------------------------------------------------------------------------------------------------------
    global turns  # count how many times ive looped
    global Pairs
    global SetPairs
    global PairsN
    turns = turns + 1  # adds a 1
   # Pairs = Pairs + 1 # adds a 1
    PairsN = PairsN = 0
    SetPairs = SetPairs
# ----------------------------------------------------------------------------------------------------------------------

   # if Pairs == 6:
       # print("well done, you got them all. you did it in", turns, "turns")
       # print("you have succesfully obtained", Pairs, "pairs, congratulations!")
       # exit()

    #if turns == 6:
        #print("well done, you got them all. you did it in", turns, "turns")
        #print("you have succesfully obtained", Pairs, "pairs, congratulations!")
       # exit()

    if userboard1 == userguess100 and userboard2 == userguess200:
        print("Both of them are a match, the first pair", userguess100, "was a", useritem2, "and the second pair",
              userguess200, "was a", useritem3)
        print("you now have", Pairs, "pair(s)")
        print("you have done", turns, "turn(s)")


    else:
        print("Both of them are not a match, the first pair", userguess100, "was a", useritem2, "and the second pair", userguess200, "was a", useritem3)
        print("you now have", PairsN, "pair(s)")
        print("you have", turns, "turn(s) so far")



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
