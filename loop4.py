print("What times table do you want?: ")
try:
    userTable = int(input())
except:
    print("Letters are not accepted, please try a number")
else:

    print("Where do you want the" ,userTable, "times table to end?: ")
    userEnd = int(input())
    print()

    for counter in range (1,userEnd+1,1):
        total = counter * userTable
        print(counter, "x", userTable, "is", total)

print("End of program")