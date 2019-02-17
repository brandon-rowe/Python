# Prime Numbers
def main():
    number = int(input("Please enter an integer to evaluate: "))
    prime(number)

def prime(number):
    if number > 1:
        for i in range(2, number-1):
            if (number % i == 0):
                print(number,"is divisible by",i)
                print(number,"is not a prime number")
                break
            else:
                print(number,"is a prime number")
                break
    else:
        print("Please enter a positive integer.")
main()
