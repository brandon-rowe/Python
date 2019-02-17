# Let's do a guessing game with random numbers.
import random

def main():
    x = eval(input("Please enter an integer from 1 to 100: "))
    y = random.randint(1, 100)
    if 1 <= x < 100:
        if x > y:
            print("You entered a value greater than the number.")
            print("X equals",x,"Y equals",y)
        elif x < y:
            print("You entered a value less than the number.")
            print("X equals",x,"Y equals",y)
    else:
        print("Please enter a digit within range.")

main()
