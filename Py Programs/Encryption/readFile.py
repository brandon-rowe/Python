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

