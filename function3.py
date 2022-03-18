def compliment():
    print("You look lovely today")

def insult():
    print("You know there is no vaccine for stupid right?")

def joke():
    print("What did the shark say when he ate a clown fish?... This tastes a little funny!")

print("1. Compliment")
print("2. Insult")
print("3. Joke")

print("Enter choice")
choice = int(input())

if choice == 1:
    compliment()

elif choice == 2:
    insult()

elif choice == 3:
    joke()

else:
    print("Out of range")
