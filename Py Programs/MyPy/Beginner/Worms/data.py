#Create test data for encryption.
#Create one large file to be encrypted.

def main():
    inp = input("Please enter your file name with extension. ")
    read(inp)
    #Input a file name with some data to be replicated over and 
    #over in the file created.

def read(inp):
    myFile = open(inp,'r')
    data = myFile.read()
    words = data.split(" ")
    print()
    print(data)
    print(words)
    write(data)

def write(data):
	i=0
	while i < 10000:
	        i += 1
	        fileName = "kronus.txt"
	        outFile = open(fileName, 'a+')
	        outFile.write(data)
	        print()
	        print(data)
	        print()
	outFile.close()

main()