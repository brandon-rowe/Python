def main():
    password = "password"
    new  = input("Please enter your new  password.")
    newcheck = input("Please re-enter password.")
    print("Current password is",password)
    if new == newcheck:
        password = new
        print("Your new password is",password)
    else:
        print("The passwords do not match. Try again.")

main()
