# Loan Qualification
def main():
    salary = float(input("Please enter your yearly Salary: "))
    if salary >= 0 and salary < 100000:
        yearsWorked = float(input("Please enter your years you have worked this job: "))
        if salary < 50000:
            print("Apologies, you do not qualify for the loan.")
        elif salary >= 50000 and yearsWorked < 2:
            print("Apologies, you do not qualify for the loan.")
        elif salary >= 50000 and yearsWorked >= 2:
            print("Congratulations! You qualify to receive the loan.")
    elif salary >= 100000:
        print("Congratulations! You qualify to receive the loan.")
    else:
        print("Please enter a valid number for salary and yearsworked")
main()
