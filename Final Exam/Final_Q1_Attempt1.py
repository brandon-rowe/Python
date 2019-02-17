def main():
    inp = str(input("Please enter a file name with extension. "))
    read(inp)

def read(inp):
    readFile = open(inp, 'r')
    data = readFile.read()
    countWord(data)
    countLines(data)
    countCharacters(data)

def countWord(data):
    count = 0
    words = data.split()
    for words in words:
        count+=1
    print("There are ",count," words in your file.")

def countLines(data):
    count = 0
    line = data.split('.')
    for line in line:
        count+=1
    print("There are ",count," lines in your file.")

def countCharacters(data):
    count = 0
    chars = data.split(" ")
    for chars in chars:
        count+=1
    print("There are ",count," characters in your file.")


main()
