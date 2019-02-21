# Factorial Program
import math
def main():
    sumNum = int(input("Please enter a factorial int: "))
    print("The Factorial is: ",math.factorial(sumNum))
    if sumNum == 0:
        print("The Factorial is: 1")
    else:
        factorial(sumNum)

def factorial(sumNum):
    n = sumNum
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("The Factorial is: ",fact) # in my screenshots, this line was indented
                # into the for loop.

    factM = (math.factorial(sumNum))
    if factM == fact:
        print("Congrats! They match! You did it!")

main()
