import random

userboard1 = random.randint(0, 10)
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

useritem = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
useritems = ["dog", "cat", "turtle", "snake", "hamster", "lion", "wolf", "monkey", "bird", "dinosaur", "dragon"]
for counter in range(0, 10):
    print(useritem[counter])

useritem2 = (useritem[userguess100]) # guess an animal for guess 1
useritem3 = (useritems[userguess200]) # guess an animal for guess 1

if "dog" in useritem and useritems:
    print("Thats a match!")



if "cat" in useritem and useritems:
    print("Thats a match")


