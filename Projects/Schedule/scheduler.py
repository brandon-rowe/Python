from datetime import date
from datetime import datetime

#replace main with GUI 
def main():
    choice = str(input("Is this for work (Ww) or personal (Pp)?"))
    if ((choice == "W") or (choice == "w")):
        work()
    elif ((choice == "P") or (choice == "p")):
        personal()
    else:
        main()

def work():
    choice = str(input("Are you clocking In (Ii), Out (Oo) or Viewing (Vv)?"))
    if ((choice == "I") or (choice == "i")):
        task = str(input("What are you working on?"))   
        writeIn(task)
    elif ((choice == "O") or (choice == "o")):
        task = str(input("What are you working on?"))
        writeOut(task)
    elif ((choice == "V") or (choice == "v")):
        readFiles()
    else:
        work()

#figuring out what to do with personal
#want to add section to account for all time
#will probably reconfigure code for purpose
def personal():
    choice = str(input("Are you clocking In (Ii), Out (Oo) or Viewing (Vv)?"))
    if ((choice == "I") or (choice == "i")):
        task = str(input("What are you working on?"))
        writeIn(task)
    elif ((choice == "O") or (choice == "o")):
        task = str(input("What are you working on?"))
        writeOut(task)
    elif ((choice == "V") or (choice == "v")):
        readFiles()
    else:
        work()

def readFiles():
    readFile = open("file.txt", 'r')
    line = 0
    for line in readFile:
        print(line)
    readFile.close()

def writeOut(task):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%H:%M:%S.%f")
    datestampStr = dateTimeObj.strftime("%d-%b-%Y")
    outfile = "Clocked Out\t " + "DATE: " + datestampStr + " \tTime: "+ timestampStr + " \tTask: " + task
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

def writeIn(task):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%H:%M:%S.%f")
    datestampStr = dateTimeObj.strftime("%d-%b-%Y")
    outfile = "Clocked In\t " + "DATE: " + datestampStr + " \tTime: "+ timestampStr + " \tTask: " + task
    writeFile = open("file.txt", 'a+')
    writeFile.write("\n")
    writeFile.write(outfile)
    writeFile.close()
    readFiles()

main()