import random

myNumber = random.randint(1, 20)
print(myNumber)

print("Guess my Number")
userGuess = int(input())

while myNumber != userGuess:
    print("Sorry that is wrong")
    userGuess = int(input())

print("Well done you guessed the right answer, which is", myNumber)
