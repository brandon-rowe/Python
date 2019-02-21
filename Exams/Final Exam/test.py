def main():
    inp = str(input("Please enter a file name with extension. "))
    readFile = open(inp, 'r')
    data = readFile.read()
    words = data.split()
    count = 0
    for words in words:
        count+=1
    print("There are ",count," words in your file.")
    count = 0
    line = data.split('.')
    for line in line:
        count+=1
    print("There are ",count," lines in your file.")
    count = 0
    for chars in data:
        count+=1
    print("There are ",count," characters in your file.")
main()
