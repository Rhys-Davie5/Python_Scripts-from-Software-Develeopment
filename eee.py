OneMetre = 6

print("Hello, Please enter the width of the room: ")
Width = float(input())
print("Please enter the length of the room: ")
Length = float(input())

Area = Width * Length
if Area < 5:
    print("The price is 6")
    print(Area * 6)
elif Area >= 5:
    print("the price is 5")
    print(Area * 5)
