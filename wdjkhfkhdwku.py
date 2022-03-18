def calculateCircle(radius):
    answer = 3.14159265359 * radius ** 2
    return answer

#---------------------------------------

def calculateSquare(side):
    area = side ** 2
    return area

#---------------------------------------

def calculateRectangle(len, width):
    area = len * width
    return area

#---------------------------------------

print("Welcome to my program")
print("Let's find the area of the first circle")
print("Enter required radius")
Area = calculateCircle(float(input()))
Area1 = round(Area, 2)
print("The area of the circle is", Area1)
print()

print("Let's find the area of the second circle")
print("Enter required radius")
Area12 = calculateCircle(float(input()))
Area14 = round(Area, 2)
print("The area of the circle is", Area14)
print()

print("lets find the area of a square")
print("Enter required side")
Area3 = calculateSquare(float(input()))
Area4 = round(Area3, 2)
print("The area of the square is", Area4)
print()

print("lets find the area of a rectangle")
print("Enter the length")
Length = float(input())
print("Enter the width")
Width = float(input())
Area5 = calculateRectangle(Length, Width)
Area6 = round(Area5, 2)
print("the area of a rectangle is", Area6)

circle_Overall = Area + Area12
square_Overall = Area3
rectangle_Overall = Area5
@@@
print("The area overall is", circle_Overall + square_Overall + rectangle_Overall)