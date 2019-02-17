class Assign4_Q5():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def _area(self):
        return self.length * self.width

newRec = Assign4_Q5(25, 15)
print(newRec._area())
#original pythonanywhere
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())