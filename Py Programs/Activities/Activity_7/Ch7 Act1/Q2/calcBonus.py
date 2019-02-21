# Calculating a Bonus
def main():
    monthlySales = float(input("Please enter your monthly sales. "))
    quota = 10000
    bonus = 0
    commissionRate = .01
    commission = commissionRate * monthlySales


    if monthlySales >= 0:
        if monthlySales < quota:
            bonus = 0
            total = commission + bonus
            print("Your bonus this month is $",bonus)
            print("Your commission is $",commission)
            print("Your total is $",total)
        elif monthlySales >= quota:
            bonus = 500
            print("Good Job!")
            print("You met your quota!")
            print("Your bonus this month is $", bonus)
            if monthlySales > 50000:
                commissionRate = .05
                total = commission + bonus
                print("Your commission is $",commission)
                print("Your total is $",total)
            else:
                total = commission + bonus
                print("Your commission is $",commission)
                print("Your total is $",total)
    else:
        print("Please enter a valid number for monthly sales.")

main()
