def enterNumber():
    theNumber = int(input())
    while theNumber < 0:
        print("Must be positive")
        theNumber = int(input())
    return theNumber


print("Enter your first number")
result = enterNumber()
print("enter your second number")
result2 = enterNumber()
print(result, result2)