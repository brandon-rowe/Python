# Purpose:  Consider a person who rolls 5 dice.  If
#           all dice are the same value, that person wins
#           and stops rolling.  If the dice are not all
#           the same value, the person picks up all 5 dice
#           and re-rolls until they get a roll of all the
#           same value.
#
#           This program simulates how many rolls are needed
#           until they win.


def main():
    # print instructions or introduction
    # get number of simulations to run, n

    # initialize total number of dice rolls to 0
    # in loop, n times
    #    run one simulation, save as rolls
    #    add that number of rolls to total
    #    print simulation number, number of rolls

    # compute the average number of dice rolls, average
    # print Average, average
    return


def diceSimulation(numDice, numSides):
    """
    Purpose:  Run one simulation to find out the number
              of rolls needed until some number of
              dice are all the same.
    Inputs:   numDice, the number of dice in each roll
              numSides, the number of sides on a die
    Returns:  The number of rolls until all the dice
              were the same, an integer.
    """
    return 0
    # roll numDice dice once
    # initialize accumulator, tries, to 1
    # while not all the same:
    #    roll the dice again
    #    add 1 to tries
    # return tries


def getDiceRoll(numDice, numSides):
    """
    Purpose:  Roll numDice numSided-dice once.
    Inputs:   numDice, the number of dice to roll.
              numSides, the number of sides each die has.
    Returns:  The results of a dice roll, a list of
              random integers.
    """
    # Create an empty list
    # Inside a loop that runs numDice times,
    #    Append one die roll to that list
    # Return the dice list
    return []

def checkAllTheSame(dice):
    """
    Purpose:  Check if a dice roll is all the same value.
    Inputs:   A list of integers, the roll of the dice.
    Returns:  A boolean, True if the dice are all the same, False otherwise.
    """
    # Get the first item, using list indexing
    # In a for loop for each item in the list
    #    If that item is not equal to the first item
    #        return False
    # If you reach the end of the for loop, return True
    return True


def runTests():
    """
    Purpose:  Test each function in the implementation here.  After
              all functions have been implemented and tested, comment
              out the call to runTests() at the bottom of the file,
              uncomment the call to main(), and start implementing main.
    Inputs:   None.
    Returns:  None.
    """
    print rollSimulation(10, 6)
    print rollSimulation(2, 30)


runTests()
#main()