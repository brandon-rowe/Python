def main():
    inp = input("Please enter your file name with extension. ")
    read(inp)

def read(inp):
    myFile = open(inp,'r')
    data = myFile.read()
    words = data.split(" ")
    print()
    print(data)
    print(words)

main()
