# Guessing Game 2
def main():
    guess = int(input("Please enter an integer between 1 & 10. "))
    secret = 4
    if guess > 0 and guess < 10:
        if guess == secret:
            print("Congratulations! You win!")
        elif guess > secret:
            print("Sorry, try again.")
            print("Your guess was too high. Try lower next time.")
        elif guess < secret:
            print("Sorry, try again.")
            print("Your guess was too low. Try higher next time.")
    else:
        print("Please enter an integer between 1 & 10 and try again.")
main()
