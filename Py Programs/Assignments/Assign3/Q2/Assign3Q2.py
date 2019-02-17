# Even Counter
def main():
    fileName = input("Please enter a .txt file name to read: (minus the .txt) ")
    readList(fileName)

def readList(fileName):
    newFile = fileName + ".txt"
    readFile = open(newFile, 'r')
    data = readFile.read()
    numbers = data.split(',')
    #numbers = data.split(" ")
    even(numbers)

def even(numbers):
    list1 = numbers
    list2 = []
    for number in list1:
        number = int(number)
        if number%2 == 0:
            list2.append(number)
        else:
            print("Not Even")

    print(list1)
    print(list2)

main()
