import random

# rule of game: get 2 identical animals to get a pair

turns = 0
countdown = 11
countdown1 = 11

def userguess():
    userboard1 = random.randint(0, 10)  # 0 is dog and 10 is dragon
    userboard2 = random.randint(0, 10)
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

    useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]  #0 1 2 3 4 5 6 7 8 9 10
    totalnolist1 = len(useritem) # 11 items

    useritem2 = (useritem[userboard1])  # get an animal for generated number 1
    useritem3 = (useritem[userboard2])  # get an animal for generated number 2
    useritem4 = (useritem[userguess100])  # get an animal for guess 1
    useritem5 = (useritem[userguess200])  # get an animal for guess 2

    global turns
    global countdownN
    turns = turns + 1
    countdown = totalnolist1 - 1
    countdownN = totalnolist1

    # useritem 2 is the first generated animal
    # useritem 3 is the second generated animal
    # useritem 4 is the first user guessed animal
    # useritem 5 is the second user guessed animal

    if len(useritem) == 0:
        print("Congratulations, you have obtained all the pairs")
        exit()

    if useritem2 and useritem3 == useritem4 and useritem5:
        print("you got a matching pair of a", useritem2, "and a", useritem3)
        useritem.remove(useritem2)  # remove generated animals
        print("the list has", countdown, "items left")
        print("you have done", turns, "turn(s)")

    else:
        print("Not a match!")
        print("the list is", totalnolist1, "items long")
        print("you have done", turns, "turn(s)")
    userguess()

print("Welcome to the pairs game! There are 6 pairs to find")
print("Here is the board")
userboard = "0 1 2 3 4 5 6 7 8 9 10"
print(userboard)
print("? ? ? ? ? ? ? ? ? ? ?")
userguess()
