import random #Imports random so I can generate random numbers in my program

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


hiddenBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",] #A list used to store the index of the three treasure locations
visibleBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",] #This list is printed for the user to see each time they have to make a guess, and is changed as the game goes on to show both correct and incorrect guesses by the user, as well as the remaining locations the user has to guess
endBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",] #Another list that is changed as the game goes on, which also stores the location of the 3 treasures that is only printed if the user loses all their guesses. Once they have, this is printed to show them what treasure locations they missed
bootyLeft = 3 #Stores the amount of treasure left to find
start = 0 #Used in the while loop at line 31 to keep looping until the user selects a difficulty, at which point 1 is added to "start" and the program continues
print("Before starting, please select a difficulty:") #Prompts user to enter difficulty
print("Easy = 10 Guesses\nMedium = 6 Guesses\nHard = 4 Guesses") #Shows user options for difficulty
while start == 0:
    difficulty = input()
    difficultyLC = difficulty.lower() #Converts the user input "difficulty" to lowercase, so the input is not case sensitive. If the user accidentally leaves their caps lock on and types "EASY", it will still go to the if statement "if difficultyLC == "easy":" as it will be converted to lower case. This is stored as
    if difficultyLC == "easy":
        guesses = 10 #Determines how many guesses the user has
        start += 1 #Adds 1 to start once difficult is correctly selected so the program will continue
    elif difficultyLC == "medium":
        guesses = 6
        start += 1
    elif difficultyLC == "hard":
        guesses = 4
        start += 1
    else:
        print("That is not a valid difficulty option, please choose your difficulty again:")
print("Ahoy 'n welcome to me booty hunt! I've lost 3 chests full o' gold that ye needs to find. But be warned! Make too many wrong guesses, 'n me 'n me crew will throw ye overboard! Good luck!")
boardSetup() #Runs the "boardSetup" function
print("Ye have to guess from 1 to 16 on the board below! (For clarification, the numbers go from left to right, so 1 is the 0 top left, 4 is the 0 top right, and 16 is be the 0 bottom right on the board.) ")
while guesses >0: #Keeps looping until guesses are not above 0
    board() #Calls the function "board"
    print("Ye 'ave", guesses, "guesses left!" ) #Tells the user how many guesses they have left
    guess = int(input()) #input for the user to enter the possible location of treasure
    guess -= 1 #Since the index of the first item in a list is 0, I allow the user to put the first location of the treasure as one, and then use this to subtract from their input, as the index of the first item in a list is actually 0. I did this to make it easier for the user to understand, as they may not know why they have to put 0 for the first location, when it makes more sense to them to input 1
    if guess >15: #Used to stop the program from crashing if the user guesses a position that is outside of the list's (hiddenBoard) index range of 0-15
        print("Where do ye see that? That location is not on the board. Try again!\n")
    elif guess <0: #Used to stop the program from crashing if the user guesses a position that is outside of the list's (hiddenBoard) index range of 0-15
        print("Where do ye see that? That location is not on the board. Try again!\n")
    elif hiddenBoard[guess] == "X": #Checks if the item at the index specified by the user in the "hiddenBoard" list contains an X
        hiddenBoard[guess] = "C" #Changes the item at the specified index in the square brackets to "C" which indicates a correct guess in the list "hiddenBoard"
        visibleBoard[guess] = "X" #Changes the item at the specified index in the square brackets to "X" which indicates a correct guess in the list "visibleBoard"
        endBoard[guess] = "C" #Changes the item at the specified index in the square brackets to "C" which indicates a correct guess in the list "endBoard"
        print("Ye found some o' me booty!")
        bootyLeft -= 1 #Subtracts 1 from bootyLeft as the user has successfully guesses the location of 1 of the treasures
        print("Ye have", bootyLeft, "of me booty left to find!\n") #Tells the user how much treasure they have left to find
        if bootyLeft == 0:
            break #Breaks from the loop if bootyLeft = 0, as there is no more treasure to find
    elif hiddenBoard[guess] == "C": #Checks if the item at the index the user guesses in the "hiddenBoard" list contains "C", as this indicates they have already correctly guessed this location
        print("Are ye pulling me peg leg? Ye already found some of me booty there. Try again!\n")
    elif visibleBoard[guess] == "/": #Checks if the item at the index the user guesses in the "hiddenBoard" list contains "/", as this indicates they have already guessed this location
        print("Ye already checked for me booty there, ye scallywag! Try again!\n")
    else:
        visibleBoard[guess] = "/" #Changes the item at the specified index in the list "visibleBoard" to a dash, to show the user where they have incorrectly guessed on the board
        endBoard[guess] = "/" #Changes the item at the specified index in the list "endBoard" to a dash, to show the user where they have incorrectly guessed on the board if they lose all their guesses
        print("Rats! Ye have guessed incorrect! That'll cost ye!")
        guesses -= 1 #Subtracts one from guesses as the user has guessed incorrectly
        print("And ye still have", bootyLeft, "of me booty left to find!\n") #Tells the user how much treasure they have left to fin

if bootyLeft == 0: #Checks if the user has won by checking if bootyLeft = 0
    board() #Calls the function "board"
    print("\nShiver me timbers! Ye've done it! Me booty is safe and sound! We'll make a pirate of ye yet!")
else:
    print("\nAaaarrrggghh! Me gold! It's all gone!...")
    print("Ye'll walk the plank for this!")
    print("\nYou lost, Unlucky! Here were the locations of the 3 treasure chests:")
    print(*endBoard[0:4], sep=" ") #lines 84-87 print the list "endBoard" to show the locations of treasure they missed
    print(*endBoard[4:8], sep=" ")
    print(*endBoard[8:12], sep=" ")
    print(*endBoard[12:16], sep=" ")
    print("Locations marked 'C' are correct guesses, locations marked '/' are incorrect guesses, and locations marked 'X' are treasure chests you missed")

