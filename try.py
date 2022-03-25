import random

def userguess():

    totalno = 10
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

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur",
                "dragon"]  # 0 1 2 3 4 5 6 7 8 9 10

    useritem2 = (useritem[userboard1])  # get the randomised number from the list
    useritem3 = (useritem[userboard2])  # get the randomised number from the list

    print(useritem2, useritem3)

    global turns
    turns = 0
    turns = turns+1


    if useritem2 == useritem3:
        useritem.remove(useritem2 and useritem3)
        print("Thats a match!")
        print("You have had", turns, "turn(s) so far")
        repeat = userguess()
        print(repeat)

    else:
        print("Not a match!")
        repeat = userguess()
        print(repeat)

    if totalno == 0:
        print("fin")


userguess()
