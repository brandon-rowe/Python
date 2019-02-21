# Chapter 9 Activity 1
# Directions: Write a program to calculate pi using the method above.
# Show the simulation process using the graphics libraryself.
#from Tkinter import *
from graphics import *
from math import *

def Rect(corner, width, height):
    corner2 = corner
    corner2.move(width, height)
    return Rectangle(corner, corner2)

def main():
    n = input("Please enter a value for n: ")
    #cirArea = math.pi * math.pow(r,2)           # area of Circle
    #sqrArea = 2*(math.pow(r,2))                 # area of square
    #cirSqrRatio = (math.pi)/4                   # cir/sqr ratio

    win = GraphWin('Draw a Rectangle (NOT!)', 300, 300)
    rect = Rect(Point(50, 50), 250, 200)
    rect.draw(win)

    win.getMouse() # Pause to view result
    win.close()
main()
