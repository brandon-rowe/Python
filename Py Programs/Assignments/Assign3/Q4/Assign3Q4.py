# Unique Elements
def main():
    fileName = input("Please enter a hyphenated string: ")
    hyphenList(fileName)

def hyphenList(fileName):
    newMsg = ""
    message = fileName.split('-')
    message.sort()
    print(message)
    for string in message:
        newMsg += string+"-"
    print(newMsg)
main()
