print("Enter your number")
userNumber = int(input())

remainder3 = userNumber % 3
remainder5 = userNumber % 5

if remainder3 == 0 and remainder5 ==0:
    print("Fizzbuzz")
elif remainder3 ==0:
    print("Fizz")
elif remainder5