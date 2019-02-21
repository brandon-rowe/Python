class Numbers(object):
    MULTIPLIER = 3
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def add(self):
        return int(self.x + self.y)

    def multiply(a):
        return int(a * int(Numbers.MULTIPLIER))

    @staticmethod
    def subtract(b, c):
        return int(b - c)

    def value(self):
        tup = (self.x, self.y)
        return tup

if __name__ == '__main__':
    test0 = Numbers(10, 2,)
    print("The results from test 0")
    print("This demonstrates the add, multipy & value methods.")
    print(test0.add())
    print(Numbers.multiply(3))
    print(test0.value())
    print('{} {}'.format(test0.x, test0.y))
    print()
    print("The results from test 1")
    print("This demonstrates the subtact static method.")
    test1 = Numbers.subtract(5, 3)
    print("The results from test 1")
    print("This demonstrates the value method that returns a tuple.")
    test2 = Numbers(10, 2)
    print(test2.add())
    print(test2.value())













#print("The results from test 1")
#print("This demonstrates the add & multipy methods.")
#    test1 = Numbers(25, 10,)
 #   print(test1.add())
  #  print(Numbers.multiply(4))
    #print('{} {}'.format(test1.x, test1.y))
#    print()
 #   print("The results from test 2")
  #  print("This demonstrates the add & multipy methods.")
   # test2 = Numbers(13, 81,)
    #print(test2.add())
#    print(Numbers.multiply(5))
 #   print('{} {}'.format(test2.x, test2.y))
