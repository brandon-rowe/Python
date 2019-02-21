# RacquetBall Simulation

from graphics import *



def main():
    
	A = input("Please enter the service ability for player A. ")
	B = input("Please enter the service ability for player B. ")
	G = int(input("Please enter the number of games to simulate. "))
	playerA = float(A)
	playerB = float(B)
	probA = randrange(0, playerA)
	probB = randrange(0, playerB)
	print("Games Simulated: ", G)
	print("Wins for A: ", playerA)
	print("Wins for B: ", playerB)
main()
	