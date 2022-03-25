import random

def userguess():
    totalno = 10
    turns = 0

    userboard1 = random.randint(0, 1) # selects random number
    userboard2 = random.randint(0, 1) # selects random number

    print(userboard1)
    print(userboard2)

    userguess100 = int(input("Please enter guess 1: ")) #userguess 1
    while userguess100 > 10:
        print("that number is too big, try a smaller number")
        userguess100 = int(input("Please enter guess 1: "))
    while userguess100 < 0:
        print("that number is too small, try a bigger number")
        userguess100 = int(input("Please enter guess 1: "))

    userguess200 = int(input("Please enter guess 2: ")) #userguess2
    while userguess200 > 10:
        print("that number is too big, try a smaller number")
        userguess200 = int(input("Please enter guess 2: "))
    while userguess200 < 0:
        print("that number is too small, try a bigger number")
        userguess200 = int(input("Please enter guess 2: "))

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
    useritems = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]

    useritem2 = (useritem[userguess100]) # get animal for guess 1
    useritem3 = (useritems[userguess200]) # get an animal for guess 1

    print(useritem2, useritem3)

    #if len(useritem and useritems):
        #print("well done, you got them all")
        #exit()

    if useritem2 == useritem3:
        useritem.remove(useritem2 and useritem3)
        totalno = totalno - 1
        turns = turns + 1
        print("Thats a match!")
        print("you have",totalno,"items left on the lsit")
        print("you have done",turns,"turns")
        repeat = userguess()
        print(repeat)


    if useritem2 != useritem3:
        totalno = totalno
        turns = turns + 1
        print("Not a match!")
        print("you have", totalno, "items left on the list")
        print("you have done", turns, "turns")
        repeat = userguess()
        print(repeat)



print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")
userboard = "0 1 2 3 4 5 6 7 8 9 10"
print(userboard)
print("? ? ? ? ? ? ? ? ? ? ?")
userguess()
