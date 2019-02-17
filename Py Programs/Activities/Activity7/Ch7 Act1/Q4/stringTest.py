# Testing Strings
def main():
    name1 = input("Please enter the first name to test: ")
    name2 = input("Please enter the second name to test: ")
    n1list = [name1,name2]
    n2list = sorted(n1list)
    print(n2list[0], n2list[1])
main()
