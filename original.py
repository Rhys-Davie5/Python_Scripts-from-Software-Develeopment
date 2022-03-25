import random
totalno = 10
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


useritem2 = (useritem[userguess100]) # get animal for guess 1
useritem3 = (useritems[userguess200]) # get an animal for guess 1

print(useritem2, useritem3)

if useritem2 == useritem3:
    print("Thats a match!")
    useritem.remove(useritem2 and useritem3)
    totalno=totalno-1

else:
    print("Not a match!")


if totalno == 0:
    print("fin")