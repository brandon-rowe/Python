# Reverse String
def main():
    s = input("Please enter a string to test: ")
    print("You entered: ",s)
    print("The reverse is: ",reverse(s))

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

main()
