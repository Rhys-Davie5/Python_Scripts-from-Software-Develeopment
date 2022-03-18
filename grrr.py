import random #library file

for counter in range (0, 10, 1):
    random1 = random.randint(1, 10)
    print(random1, end=" ")
print()
print()
random2 = random.random() #between 0 and 1
random2 = random2 * 100 #formula
print(random2)

