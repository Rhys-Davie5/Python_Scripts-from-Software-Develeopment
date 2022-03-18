import random

random1 = random.randint(1, 2)
random2 = random.randint(1, 2)
random3 = random.randint(1, 2)

print(random1, random2, random3)

if (random1 == random2 and random2 == random3):
    print("All the elements are Equal")
else:
    print("Elements are not equal")



