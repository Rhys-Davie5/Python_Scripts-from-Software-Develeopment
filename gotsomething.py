import random

def userguess():
    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
    totalnolist1 = len(useritem)
    turns = 0

    userboard1 = random.randint(1, 11)  # selects random number
    userboard2 = random.randint(1, 11)  # selects random number

    print(userboard1)
    print(userboard2)

    userguess100 = int(input("Please enter guess 1: ")) #userguess 1
    while userguess100 > 11:
        print("that number is too big, try a smaller number")
        userguess100 = int(input("Please enter guess 1: "))
    while userguess100 < 0:
        print("that number is too small, try a bigger number")
        userguess100 = int(input("Please enter guess 1: "))

    userguess200 = int(input("Please enter guess 2: ")) #userguess2
    while userguess200 > 11:
        print("that number is too big, try a smaller number")
        userguess200 = int(input("Please enter guess 2: "))
    while userguess200 < 0:
        print("that number is too small, try a bigger number")
        userguess200 = int(input("Please enter guess 2: "))

    useritem2 = (useritem[userboard1]) # get animal for guess 1 dog or cat
    useritem3 = (useritem[userboard2]) # get an animal for guess 1 cat or dog

    if useritem2 == useritem3:
        useritem.remove(useritem2 and useritem3)
        turns=turns + 1
        print("Thats a match!")
        print("you have",totalnolist1-1,"items left on the list")
        print("you have done",turns,"turn(s)")
        repeat = userguess()
        print(repeat)


    else:
        turns = turns + 1
        print("Not a match. the first pair was a" ,useritem2, "and the second number was a" ,useritem3)
        print("you have", totalnolist1, "items left on the list")
        print("you have done", turns, "turns")
        repeat = userguess()
        print(repeat)



print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")
userboard = "0 1 2 3 4 5 6 7 8 9 10 11"
print(userboard)
print("? ? ? ? ? ? ? ? ? ? ? ?")
userguess()
