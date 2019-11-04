def main():
    _wage = float(input("Please enter your hourly wage: "))
    _hours = float(input("Please enter your weekly hours: "))
    _taxDep = int(input("Please enter your number of dependents: "))

    regHours = 40
    ovTimeHrs = _hours - regHours
    ovTimeWage = _wage * 1.5
    regPay = _wage * _hours
    ovTimePay = (ovTimeWage * ovTimeHrs) + (_wage * regHours)

    if 0 <= _taxDep < 10:
        if _taxDep == 0:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _0depTax = regPay - (regPay * .21)
                print("Your weekly pay is around $", _0depTax, "after taxes.")
            elif _hours > regHours:
                _0depTax = ovTimePay - (ovTimePay * .21)
                print("Your weekly pay is around $", _0depTax, "after taxes.")
        elif _taxDep == 1:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _1depTax = regPay - (regPay * .20)
                print("Your weekly pay is around $", _1depTax, "after taxes.")
            elif _hours > regHours:
                _1depTax = ovTimePay - (ovTimePay * .20)
                print("Your weekly pay is around $", _1depTax, "after taxes.")
        elif _taxDep == 2:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _2depTax = regPay - (regPay * .19)
                print("Your weekly pay is around $", _2depTax, "after taxes.")
            elif _hours > regHours:
                _2depTax = ovTimePay - (ovTimePay * .19)
                print("Your weekly pay is around $", _2depTax, "after taxes.")
        elif _taxDep == 3:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _3depTax = regPay - (regPay * .18)
                print("Your weekly pay is around $", _3depTax, "after taxes.")
            elif _hours > regHours:
                _3depTax = ovTimePay - (ovTimePay * .18)
                print("Your weekly pay is around $", _3depTax, "after taxes.")
        elif _taxDep == 4:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _4depTax = regPay - (regPay * .17)
                print("Your weekly pay is around $", _4depTax, "after taxes.")
            elif _hours > regHours:
                _4depTax = ovTimePay - (ovTimePay * .17)
                print("Your weekly pay is around $", _4depTax, "after taxes.")
        elif _taxDep == 5:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _5depTax = regPay - (regPay * .16)
                print("Your weekly pay is around $", _5depTax, "after taxes.")
            elif _hours > regHours:
                _5depTax = ovTimePay - (ovTimePay * .16)
                print("Your weekly pay is around $", _5depTax, "after taxes.")
        elif _taxDep == 6:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _6depTax = regPay - (regPay * .15)
                print("Your weekly pay is around $", _6depTax, "after taxes.")
            elif _hours > regHours:
                _6depTax = ovTimePay - (ovTimePay * .15)
                print("Your weekly pay is around $", _6depTax, "after taxes.")
        elif _taxDep == 7:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _7depTax = regPay - (regPay * .14)
                print("Your weekly pay is around $", _7depTax, "after taxes.")
            elif _hours > regHours:
                _7depTax = ovTimePay - (ovTimePay * .14)
                print("Your weekly pay is around $", _7depTax, "after taxes.")
        elif _taxDep == 8:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _8depTax = regPay - (regPay * .13)
                print("Your weekly pay is around $", _8depTax, "after taxes.")
            elif _hours > regHours:
                _8depTax = ovTimePay - (ovTimePay * .13)
                print("Your weekly pay is around $", _8depTax, "after taxes.")
        elif _taxDep == 9:
            if _hours < 0:
                print("Please enter a valid number of hours")
            elif _hours <= regHours:
                _9depTax = regPay - (regPay * .12)
                print("Your weekly pay is around $", _9depTax, "after taxes.")
            elif _hours > regHours:
                _9depTax = ovTimePay - (ovTimePay * .12)
                print("Your weekly pay is around $", _9depTax, "after taxes.")
    else:
        print("Please enter a valid dependent value between 0 - 9 and try again.")
main()
