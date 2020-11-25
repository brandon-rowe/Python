from datetime import date
from datetime import datetime

#replace main with GUI 
def main():
    choice = str(input("Are you clocking In (Ii), Out (Oo) or Viewing (Vv)?"))
    if choice == "I":
        writeIn()
    elif choice == "i":
        writeIn()
    elif choice == "O":
        writeOut()
    elif choice == "o":
        writeOut()
    elif choice == "V":
        readFies()
    elif choice == "v":
        readFiles()
    else:
        main()

def readFiles():
    readFile = open("file.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()

def writeOut():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%H:%M:%S.%f)")
    datestampStr = dateTimeObj.strftime("%d-%b-%Y")
    outfile = "Clocked out at " + timestampStr + " on " + datestampStr
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

def writeIn():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%H:%M:%S.%f)")
    datestampStr = dateTimeObj.strftime("%d-%b-%Y")
    outfile = "Clocked in at " + timestampStr + " on " + datestampStr
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

main()