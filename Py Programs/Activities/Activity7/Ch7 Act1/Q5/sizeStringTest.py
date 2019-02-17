#String Size Compare
def main():
    name1 = input("Please enter a name: ")
    name2 = input("Please enter another name: ")
    n1 = len(name1)
    n2 = len(name2)
    if n1 > n2:
        print(name1, name2)
    else:
        print(name2, name1)
main()
