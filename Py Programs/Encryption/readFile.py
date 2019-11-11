def main():
    inp = str(input("Please enter a file name with extension. "))
    readFile = open(inp, 'r')
    lines=0
    words=0
    characters=0
    for line in readFile:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
    print("There are %s words, %s lines and %s characters in your file." % (words, lines, characters))
main()


#print("There are ",words," words in your file.")
#print("There are ",lines," lines in your file.")
#print("There are ",characters," characters in your file.")


#data = readFile.read()
#    words = data.split()
#    count = 0
#    for words in words:
#        count+=1
#    print("There are ",count," words in your file.")
#    countLine = 0
#    line = data.split('.')
#    for line in line:
#        countLine+=1
#    print("There are ",countLine," lines in your file.")
#    countChars = 0
#    for chars in data:
#        countChars+=1
#    print("There are ",countChars," characters in your file.")