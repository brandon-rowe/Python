import graphics *

def main():
    win = GraphWin("Click Me!") 
    p = win.getMouse() 
    print("You clicked", p.getX(), p.getY())
main()
