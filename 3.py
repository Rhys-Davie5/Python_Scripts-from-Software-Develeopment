Veg = ["Apple", "Bananas", "Pear", "Peach", "Grapes", "Brussel Sprouts", "Brocolli"]
Dairy = ["Milk", "Bread"]

userChoice = input("What vegatable do you want?")

for counter in range(0, len(Veg) ,1):
    if Veg[counter] == userChoice:
        print(userChoice,"s number is",Dairy[counter])




