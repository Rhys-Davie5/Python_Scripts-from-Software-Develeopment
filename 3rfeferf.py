monday = float(input("Enter miles for Monday: "))
while monday < 0:
    print("Please try again")
    monday = float(input("Enter miles for Monday: "))


tuesday = float(input("Enter miles for Tuesday: "))
while tuesday < 0:
    print("Please try again")
    tuesday = float(input("Enter miles for Tuesday: "))


wednesday = float(input("Enter miles for Wednesday: "))
while wednesday < 0:
    print("Please try again")
    wednesday = float(input("Enter miles for Wednesday: "))


thursday = float(input("Enter miles for Thursday: "))
while thursday < 0:
    print("Please try again")
    thursday = float(input("Enter miles for Thursday: "))

friday = float(input("Enter miles for Friday: "))
while friday < 0:
    print("Please try again")
    friday = float(input("Enter miles for Friday: "))


saturday = float(input("Enter miles for Saturday: "))
while saturday < 0:
    print("Please try again")
    saturday = float(input("Enter miles for Saturday: "))


sunday = float(input("Enter miles for Sunday: "))
while sunday < 0:
    print("Please try again")
    sunday = float(input("Enter miles for Sunday: "))

litre = 1.35
miles_to_litre = 11.2
weekTotal = monday + tuesday + wednesday + thursday + friday + saturday + sunday
miles1 = weekTotal / miles_to_litre * litre
miles2 = round(miles1, 2)

print("The total mileage was: ",weekTotal, "miles")
print("Cost of petrol: ", "£",miles2)
