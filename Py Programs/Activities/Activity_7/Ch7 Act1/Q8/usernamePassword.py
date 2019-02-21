#Username & Password check.
def main():
    userName = "benedict"
    password = "arnold"
    userInput = input("Please enter the username: ")
    userPass = input("Please enter the password: ")
    if userName == userInput:
        if password == userPass:
            print("Login Success!")
        else:
            print("Login Failed.")
    else:
        print("Login Failed.")
main()
