# monty.py
import random

def main():
    printIntro()
    result = simNGames()
    printResults(result)

def printIntro():
    print()
    print("The Monty Hall Problem")
    print('A contestant is faced with three doors. ')
    print("Behind one door is a very large prize.")
    print("The contestant tries to guess which door has the prize. ")
    print()
    print("This program simulates multiple Monty Hall Problems")
    print("to determine if the odds match up.")

def simOneGame():
    c = random.randint(1,3)
    r = [1,2,3]
    for i in r:
        if i == c:
            r.remove(i)
    w = random.choice(r)
    c = random.choice(r)
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
    result = (wins/n)*100
    return result

def printResults(result):
    print("Your simulation won %s percent of the time." %(result))
    print("Expection was for 30%.")

if __name__ == '__main__': main()