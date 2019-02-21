#ReadAndWrite program
def main():
    myFile = open("myFile.txt",'r')
    data = myFile.read()
    words = data.split(" ")
    numWords = len(words)
    print()
    print(data)
    print()
    print("Total number of words:",numWords)
    myFile.close()
    numWords = str(numWords)

    outFile = open("newFile.txt", 'w')
    outFile.write(data)
    outFile.write("Number of words:")
    outFile.write(numWords)

    print()
    outFile.close()

main()

#    myFile = open("myFile.txt",'r')
#    data = myFile.read()
#    words = data.split(" ")
#    numWords = len(words)
#    print(data)
#    print("Total number of words:",numWords)
#    myFile.close()
#    numWords = str(numWords)

#    outFile = open("newFile.txt", 'w')
#    outFile.write(data)
#    outFile.write(" ")
#    outFile.write("Number of words:")
#    outFile.write(numWords)
#    outFile.close()
