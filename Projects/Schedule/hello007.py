#hello 007

def main():
    print("\nMoneyPenny say's these are your pressing matters:\n")
    readFile = open("todo.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()
main()