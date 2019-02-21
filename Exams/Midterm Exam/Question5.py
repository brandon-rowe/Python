# Character Counter
def main():
    word = input("Please enter a word to be evaluated: ")
    x = input("Please enter a letter to count within word: ")
    xCount = 0
    for ch in word:
        if ch == x:
            xCount += 1
    if xCount == 0:
        print("There are no instances of",x,"in",word)
    else:
        print("There are",xCount,"instances of the letter",x,"in",word)
main()
