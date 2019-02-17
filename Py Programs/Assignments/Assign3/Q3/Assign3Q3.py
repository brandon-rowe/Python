# Palindrome String
def main():
    s = input("Please enter a string to test: ")
    print("You entered: ",s)
    print("The reverse is: ",reverse(s))
    print("Palindrome is: ", palindrome(s, str))

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def palindrome(s, str):
    if s == reverse(s):
        return True
    else:
        return False

main()
