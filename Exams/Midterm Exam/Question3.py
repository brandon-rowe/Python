# Checksum Calculator
def main():
    # Get the message to encode
    message = input("Please enter the message to encode: ")
    total = 0
    checksum = 0
    # Loop through the message and print out the Unicode values
    newMsg = ""
    for ch in message:
        newMsg = newMsg + str(ord(ch))
        print(ord(ch),  end=" ")
        num = int(ord(ch))
        total += num
    print()  # blank line before prompt
    checksum = total%10
    print("Your Checksum Value:",checksum)
main()
