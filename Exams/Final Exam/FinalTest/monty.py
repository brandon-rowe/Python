# monty.py
import random

def main():
    printIntro()
    simNGames()

def printIntro():
    print()
    print("The Monty Hall Problem")
    print('A contestant is faced with three doors. ')
    print("Behind one door is a very large prize (say, a car).")
    print("The contestant tries to guess which door has the prize. ")
    print()

def simOneGame():
    c = random.randint(1,3)
    w = random.randint(1,3)
    if c == w:
        win = True
    else:
        win = False
    return win

def simNGames():
    n = 50
    wins = 0
    for i in range(n):
        win = simOneGame()
        if win == True:
            wins+=1
    result = 100(wins/n)
    return result

def printResults(chosen, winning, result):
    if result == True:
        print("You chose %s and the game chose %s." % (chosen, winning))
        print("Monty!")
    else:
        print("You chose door number %s " % (chosen))
        print("You should've gone for door number %s " % (winning))
        print("Sorry, you lose this round.")


if __name__ == '__main__': main()