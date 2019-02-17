# Future Value Program

def main():
    _principalAmt = eval(input("Please enter your principal amount:  "))
    _APR = eval(input("Please enter your APR as a decimal:  "))
    _investYears = eval(input("Please enter the years to invest:  "))


    for i in range(_investYears):
        _interest = (_principalAmt * (1 + _APR))
        _principalAmt = _interest
    print("You will have a balance of",_principalAmt, "after", i + 1,"years.")

main()
