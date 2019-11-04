from graphics import *
def main():
    win = GraphWin()

    for i in range(4):
        rect = Rectangle(Point(i*50,i*50)),Point((i+1)*50,(i+1)*50)
        rect = setFill("black")
        rect.setOutlin("black")
        rect.draw(win)

main()
