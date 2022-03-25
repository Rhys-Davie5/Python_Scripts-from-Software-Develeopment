import random
turns = 0
def userguess():
    userboard1 = random.randint(0, 0)
    userboard2 = random.randint(0, 0)
    print(userboard1)
    print(userboard2)

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

    global turns
    turns = turns + 1

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
    totalnolist1 = len(useritem)

    useritem2 = (useritem[userboard1])  # get an animal for generated number 1
    useritem3 = (useritem[userboard2])  # get an animal for generated number 2
    useritem4 = (useritem[userguess100]) # get an animal for guess 1
    useritem5 = (useritem[userguess200]) # get an animal for guess 2

    print("this is the randomised animal",useritem2)
    print("this is the randomised animal",useritem3)

    if useritem2 and useritem3 == useritem4 and useritem5:
        print("you got a matching pair of a",useritem2,"and a",useritem3)
        print("the list is", totalnolist1, "items long")
        print("you have done", turns, "turn(s)")
        useritem.remove(useritem2)
        userguess()

    else:
        print("Not a match!")
        print("you have done", turns, "turn(s)")
        print()
        userguess()


userguess()