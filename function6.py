print("Hellow and welcome to my program!")

def userAssignment(userScore):
    if userScore > 100:
        print("out of range")
    elif userScore >= 80:
        print("Wow well done, you got a distinction!")
    elif userScore >= 70:
        print("You got a Merit!")
    elif userScore >= 50:
        print("You got a pass")
    elif userScore <= 40:
        print("Im sorry but you failed this assignment")

print("What mark out of 100 did you get for assignment 1?")
userScore1 = int(input())
userAssignment(userScore1)