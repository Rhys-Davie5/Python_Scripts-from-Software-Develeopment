def add(no1, no2):
    total = no1 + no2
    return total
#-------------------------------------------
def sub(no1,no2):
    total1 = no2 - no1
    return total1
#-------------------------------------------



print("Welcome to the calculator program\n")
print("Enter your first number: ")
value1 = int(input())
print("Enter your second number: ")
value2 = int(input())

print("\nMenu - what would you like to do?")
print("1. Add your numbers")
print("2. Subtract the second number from the first")

print("\nEnter your choice:")
choice = int(input())

if choice == 1:
    print("\nLet's add them...")
    #  Function call will go here
    result = add(value1, value2)
    print("its", result)

elif choice == 2:
    print("Lets subtract them")
    result1 = sub(value2, value1)
    print("its", result1)




print("\nEnd of program")
