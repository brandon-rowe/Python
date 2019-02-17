# Future Value Program

def main():
    _principalAmt = eval(input("Please enter your principal amount:  "))
    _APR = eval(input("Please enter your APR:  "))
    _investYears = eval(input("Please enter the years for investment:  "))
    _output = (_principalAmt * (1 + _APR))

    for i in range(_investYears):
        _output += _output
        print(_output)

main()
