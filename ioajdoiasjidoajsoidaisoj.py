milage =float(0)
amount =float(0)
variable = ["Monday","Tuesday","Wednesday","Thursday","Friday","saturday","Sunday"]
for x in range (7):
        print("enter miles for",variable[x])
        amount = float(input())
        while amount < 0:
            print("please try again")
            print("enter miles for",variable[x])
            amount = float(input())
        milage = milage + amount
litre=milage/11.2
print("The total milage was:",milage)
print("Cost of petrol:",litre*1.35)
