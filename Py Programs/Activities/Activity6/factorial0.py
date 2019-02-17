# Factorial Program
import math
def main():
    sumNum = int(input("Please enter a factorial int: "))
    print("The Factorial is: ",math.factorial(sumNum))
    factorial(sumNum)

def factorial(sumNum):
    n = sumNum
    fact = 1
    if n == 0:
        fact = 1
        print("1")
    else:
        for i in range(1, n+1):
            fact = fact * i
            print(fact)

    factM = (math.factorial(sumNum))
    if factM == fact:
        print("You did it!")

main()
