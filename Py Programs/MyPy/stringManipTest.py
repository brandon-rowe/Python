
def main():
    _q = str(input("Please enter a number of Quarters: "))
    _d = str(input("Please enter a number of Dimes: "))
    _n = str(input("Please enter a number of Nickels: "))
    _p = str(input("Please enter a number of Pennies: "))
    _s = str(input("How much do you need to spend for purchase? "))

    _q = float(_q)
    _d = float(_d)
    _n = float(_n)
    _p = float(_p)
    _s = float(_s)

    _pennies = _p * .01
    _nickels = _n * .05
    _dimes = _d * .10
    _quarters = _q * .25
    _total = _pennies + _nickels + _dimes + _quarters
    _leftOver = _total - _s

    if _s <= _total:
        print(_p,"pennies =",_pennies,"cents.")
        print(_n,"nickels =",_nickels,"cents.")
        print(_d,"dimes =",_dimes,"cents.")
        print(_q,"quarters =",_quarters,"cents.")
        print("Your total is $", _total)
        print("You are spending $", _s)
        print("You can make this purchase!")
        print("You will have $",_leftOver,"after your purchase.")
    else:
        print(" ",_total)
        print("-", _s)
        print("=", _leftOver)
        print("You do not have enough monies.")

main()
