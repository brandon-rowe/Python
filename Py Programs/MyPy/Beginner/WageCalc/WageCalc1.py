def main():
    _wage = eval(input("Please enter your hourly wage: "))
    _hours = eval(input("Please enter your weekly hours: "))
    _taxDep = eval(input("Please enter your number of dependents: "))

    regHours = 40
    ovTimeHrs = _hours - regHours
    ovTimeWage = _wage * 1.5
    regPay = _wage * _hours
    ovTimePay = (ovTimeWage * ovTimeHrs) + (_wage * regHours)

    if _taxDep == 0:
        if _hours < 0:
            print("Please enter a valid number of hours")
        elif _hours <= regHours:
            _0depTax = regPay - (regPay * .23)
            print("Your weekly pay is around $", _0depTax, "after taxes.")
        elif _hours > regHours:
            _0depTax = ovTimePay - (ovTimePay * .23)
            print("Your weekly pay is around $", _0depTax, "after taxes.")
    elif _taxDep == 1:
        if _hours < 0:
            print("Please enter a valid number of hours")
        elif _hours <= regHours:
            _1depTax = regPay - (regPay * .21)
            print("Your weekly pay is around $", _1depTax, "after taxes.")
        elif _hours > regHours:
            _1depTax = ovTimePay - (ovTimePay * .21)
            print("Your weekly pay is around $", _1depTax, "after taxes.")

main()
