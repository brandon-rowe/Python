# Guessing Game 1
def main():
    guess = int(input("Please guess an integer between 1 & 10. "))
    secret = 4
    if guess >= 1 and guess <= 10:
        if guess == secret:
            print("Congratulations! You win!")
        elif guess < secret:
            print("Your number is below the number. Try again.")
        elif guess > secret:
            print("Your number is above the number. Try again.")
    else:
        print("Please enter a number between 1 & 10.")
main()
