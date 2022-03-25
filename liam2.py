import random

def bootyPlacement(): #Function for randomly selecting the treasures location
    successfulReplacement = 1 #Used for the while loop in this function
    while successfulReplacement == 1: # While loop that loops until successfulReplacement does not equal 1
        randomNum = random.randint(0, 11) #random.randint is used to generate a random number, the 2 numbers in the brackets is the range of the random number generator
        if hiddenBoard[randomNum] == "0": #Checks if the item in "hiddenBoard" at the specified index in the square brackets stores the string 0. (RandomNum is used to the index is randomised each time the function is run) This statement is used to check if the index specified has an X already stored, and if there is, it will loop again until the index randomly generated is unique.
            hiddenBoard[randomNum] = "X" #Changes the item stored at the index to an X which is the symbol I use for treasure on the board
            endBoard[randomNum] = "X" #Adds the "treasure" to another list called "endBoard" which is printed at the end of the code if the user is unsuccessful in guessing all three locations of treasure, to show the user what treasure they missed
            successfulReplacement -= 1 #Allows the loop to finish once the index of the treasure is generated and is unique from other locations of treasure previously generated

def boardSetup(): #A function that runs the function "bootyReplacement" 3 times to select 3 different locations of treasure
    bootyPlacement() #Runs the function "bootyPlacement"
    bootyPlacement()
    bootyPlacement()

def board(): #A function that sets up the board. This was made so I could tidy up my if statements later on as I have many if statements, and this allows me to run 4 lines of code in one by running this function instead
    print(*visibleBoard[0:4], sep=" ") #* Unpacks the list (visibleBoard), sep=" " seperates each item in the list with a space. This makes the board more p[leasing to look at, as this will print the list with the square brackets and quotation marks.
    print(*visibleBoard[4:8], sep=" ") #I also wanted to print the list 4 items at a time, to make the list look more like a board, so I specified the index range I wanted to print in the square brackets. This meant each line would print four items form the list and make it more aesthetically pleasing to look at
    print(*visibleBoard[8:12], sep=" ")
    print(*visibleBoard[12:16], sep=" ")

print("Ahoy 'n welcome to me booty hunt! I've lost 3 chests full o' gold that ye needs to find. But be warned! Make too many wrong guesses, 'n me 'n me crew will throw ye overboard! Good luck!")
print("Ye have to guess from 1 to 16 on the board below! (For clarification, the numbers go from left to right, so 1 is the 0 top left, 4 is the 0 top right, and 16 is be the 0 bottom right on the board.) ")
while guesses >0:
    print("Ye 'ave", guesses, "guesses left!" )
    guess = int(input())
    guess -= 1
    if bootyLeft == 0:
            break #Breaks from the loop if bootyLeft = 0, as there is no more treasure to find
    elif hiddenBoard[guess] == "C": #Checks if the item at the index the user guesses in the "hiddenBoard" list contains "C", as this indicates they have already correctly guessed this location
        print("Are ye pulling me peg leg? Ye already found some of me booty there. Try again!\n")
    elif visibleBoard[guess] == "/": #Checks if the item at the index the user guesses in the "hiddenBoard" list contains "/", as this indicates they have already guessed this location
        print("Ye already checked for me booty there, ye scallywag! Try again!\n")
    else:
        print("And ye still have", bootyLeft, "of me booty left to find!\n") #Tells the user how much treasure they have left to fin

if bootyLeft == 0:
    print("Shiver me timbers! Ye've done it! Me booty is safe and sound! We'll make a pirate of ye yet!")
else:
    print("Aaaarrrggghh! Me gold! It's all gone!...")
