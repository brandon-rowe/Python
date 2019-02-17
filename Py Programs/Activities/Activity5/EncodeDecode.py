# text2numbers.py
# Encoder
#     A program to convert a textual message into a sequence of
#         numbers, utlilizing the underlying Unicode encoding.

def main():
    print("This program converts a textual message into a sequence")
    print ("of numbers representing the Unicode encoding of the message.\n")

    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    newMsg = ""
    for ch in message:
        newMsg = newMsg + str(ord(ch)) + " "
        print(ord(ch),  end=" ")
    print()  # blank line before prompt
    print("New string concat created from for loop: ",newMsg)

    message = ""
    for numStr in newMsg.split():
        # convert the (sub)string to a number
        codeNum = int(numStr)
        # append character to message
        message = message + chr(codeNum)

    print("\nThe decoded message is:", message)
main()
