# Unique Elements 
def main():
    fileName = input("Please enter a .txt file name to read (minus the .txt): ")
    readList(fileName)

def readList(fileName):
    newFile = fileName + ".txt"
    readFile = open(newFile, 'r')
    data = readFile.read()
    numbers = data.split(',')
    #numbers = data.split(" ")
    unique(numbers)

def unique(numbers):
    list1 = numbers
    list2 = []
    for number in list1:
        if number in list2:
            print("Number repeated.")
        else:
            list2.append(number)
    print(list1)
    print(list2)

main()
