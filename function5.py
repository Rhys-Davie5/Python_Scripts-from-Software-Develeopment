def confirmation(postcode, houseNumber):
    print("we will deliver to",houseNumber,postcode)

print("Thank you for ordering!")
print()
print("Please enter your postcode")
Postcode = input()
print("Please enter your house number")
houseNumber = input()

confirmation(Postcode, houseNumber)