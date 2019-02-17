# Unique Elements
def main():
    number = int(input("Please enter an integer to evaluate "))
    prime(number)

def prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number,"is not a prime number")
        else:
            print(number,"is a prime number")
    else:
        print("Please enter a positive integer.")
main()
