print("Enter day: ")
userDay =int( input())
print("Enter Month: ")
userMonth = input()
print("Enter Year: ")
userYear = int(input())

print(userDay)

if userDay==1 or userDay==21 or userDay ==31:
    print("st")
elif userDay==2 or userDay==22:
    print("nd")
