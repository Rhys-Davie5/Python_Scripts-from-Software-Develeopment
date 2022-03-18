print("Where do you want to start?: ")
userStart = int(input())

print("When do you want it to stop?: ")
userEnd = int(input())


for userNumber in range(userStart, userEnd+1, 1):
    print(userNumber)