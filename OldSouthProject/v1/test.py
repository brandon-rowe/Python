def main():
    view1 = "V"
    view2 = "v"
    choice = input("Would you like to view or add files? ('Vv' or 'Aa')")
    print(choice)
    if choice == view1:
        print("success view 1")
    elif choice == view2:
        print("success view 2")
    else:
        print("Fail")
main()


    #num = 5
    #for x in range(num):