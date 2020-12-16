def main():
    choice = str(input("Would you like to view or add files? ('Vv' or 'Aa')"))
    if choice == "V":
        readFiles()
    elif choice == "v":
        readFiles()
    elif choice == "A":
        enterFiles()
    elif choice == "a":
        enterFiles()
    else:
        main()

def readFiles():
    readFile = open("file.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()

def enterFiles():
    orderNum = str(input("Order number: "))
    custName = str(input("Customer name: "))
    shipVia = str(input("Ship via: "))
    orderDate = str(input("Order entry date: "))
    print(orderNum, custName, shipVia, orderDate)
    writeFile(orderNum, custName, shipVia, orderDate)

def writeFile(orderNum, custName, shipVia, orderDate):
    stringFile = orderNum + "\t\t" + custName + "\t\t\t" + shipVia + "\t\t" + orderDate
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(stringFile)
    writeFile.close()
    readFiles()

main()