# customer.py
# customer class
class Customer:
    def __init__(self, name, uname, pword, balance):
        self.name = name
        self.uname = uname
        self.pword = pword
        self.balance = balance

    def withdraw(self, witAmt):
        self.balance -= witAmt

    def deposit(self, depAmt):
        self.balance += depAmt

    def checkBalance(self):
        print("Your balance is ", self.balance)

    def toString(self):
        print("Hello ", self.name)
        print("Your username is ", self.uname)
        print("Your password is ", self.pword)
        print("Your balance is ", self.balance)

def main():
    customer1 = Customer("Brandon", "bran", "pword", 1000.00)
    customer1.deposit(100)
    customer1.withdraw(150)
    customer1.toString()
    customer1.name
    customer2 = Customer("Conner", "conmur", "pword1", 2000.00)
    customer2.deposit(100)
    customer2.withdraw(150)
    customer2.toString()
    customer2.name
    customer3 = Customer("Josh", "jhow", "pword2", 3000.00)
    customer3.deposit(100)
    customer3.withdraw(150)
    customer3.toString()
    customer3.name

if __name__ == "__main__":
    main()
