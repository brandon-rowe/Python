#ReadAndWrite program
def main():
    myFile = open("myFile.txt",'r')
    data = myFile.read()
    words = data.split(" ")
    print()
    print(data)
    print(words)
    myFile.close()

    outFile = open("newFile.txt", 'w')
    outFile.write(data)
    print()
    print(data)
    print()
    outFile.close()

main()
