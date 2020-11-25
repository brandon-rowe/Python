import time
import datetime
import calendar
from datetime import date
from datetime import datetime

def main():
    choice = str(input("Are you clocking In (Ii) or Out (Oo)?"))
    if choice == "I":
        writeIn()
    elif choice == "i":
        writeIn()
    elif choice == "O":
        writeOut()
    elif choice == "o":
        writeOut()
    else:
        main()

def readFiles():
    readFile = open("file.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()

#def enterFiles():
#    orderNum = str(input("Order number: "))
#    custName = str(input("Customer name: "))
#    shipVia = str(input("Ship via: "))
#    orderDate = str(input("Order entry date: "))
#    print(orderNum, custName, shipVia, orderDate)
#    writeFile(orderNum, custName, shipVia, orderDate)

def writeOut():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    outfile = "Clocked out at " + timestampStr
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

def writeIn():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%H:%M:%S.%f)")
    datestampStr = dateTimeObj.strftime("%d-%b-%Y")
    outfile = "Clocked in at " + timestampStr
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

main()