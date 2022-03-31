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

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]



    useritem2 = (useritem[userguess100 and userguess200]) # get an animal for guess 1 and 2
    useritem3 = (useritem[userguess200]) # get an animal for guess 2

    totalnolist1 = len(useritem)

    print(useritem2, useritem3)
    global turns
    turns = turns + 1

    if useritem2 == useritem3:
        useritem.remove(useritem2)
        print("Its a match")
        print("the list is" ,totalnolist1, "long")
        print("you have done", turns, "turn(s)")
        userguess()

    else:
        print("Not a match!")
        print("you have done", turns, "turn(s)")
        print()
        userguess()



    #if totalno == 0:
        #print("fin")

userguess()