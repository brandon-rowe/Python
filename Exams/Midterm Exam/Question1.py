# Change Counter
def main():
        _change = int(input("Please enter an amount between 0-99: "))

        _quarters =  _change//25
        _change = _change%25
        _dimes = _change//10
        _change = _change%10
        _nickels = _change//5
        _change = _change%5
        _pennies = _change//1

        print(_quarters,": Quarters")
        print(_dimes,": Dimes")
        print(_nickels,": Nickels")
        print(_pennies,": Pennies")

main()
