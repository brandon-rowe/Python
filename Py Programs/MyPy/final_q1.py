# Word Count
# Takes in filename to open, read and count words in file.

def main():
    fileName = input("Please enter a filename with extension.")
    file = open(fileName,"r")
    data = file.read()
    words = data.split()
    count=0
    for words in data:
        print(str)
        count+=1
    print(count)
    file.close()

main()