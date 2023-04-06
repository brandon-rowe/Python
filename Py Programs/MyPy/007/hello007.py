#hello 007

def main():
    print("\nMessage from M: Goodmorning 007")
    print("\nThe people trying to make this world worse are not taking a day off, neither can you.")
    print("\n1. Print your task list?")
    print("2. Print Affirmations")
    command = str(input("Where would you like to start? "))
    if command == "Tasks":
        todo()
    elif command == "tasks":
        todo()
    elif command == "Affirm":
        affirm()
    elif command == "affirm":
        affirm()
    else:
        main()

def todo():
    print("\nMoneyPenny say's these are your pressing matters:\n")
    readFile = open("todo.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()

def affirm():
    print("You are the man")

main()