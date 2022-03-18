PI = 3.14

print("Please enter radius of circle: ")
circleRadius = int(input())

while circleRadius > 10:
    print("This number is a little big, please try again")
    circleRadius = float(input())

print("Please enter the side of the square: ")
sideSquare = int(input())

while sideSquare > 10:
    print("This number is a little big, please try again")
    sideSquare = int(input())


print("Please enter the width of the rectangle: ")
widthRectangle = int(input())

while widthRectangle > 10:
    print("This number is a little big, please try again")
    widthRectangle = int(input())


print("Please enter the length of the rectangle: ")
lengthRectangle = input()

while lengthRectangle > 10:
    print("This number is a little big, please try again")
    lengthRectangle = int(input())


Area = PI * circleRadius * circleRadius
print("The Area of the circle is = %.2f" %Area ,"cm")