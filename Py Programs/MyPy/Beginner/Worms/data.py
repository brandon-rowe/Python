#Create test data for encryption.
#Create one large file to be encrypted.
import time

def main():
    inp = input("Please enter your file name with extension. ")
    start_time = time.time()
    read(inp)
    #Input a file name with some data to be replicated over and 
    #over in the file created.

def read(inp):
    myFile = open(inp,'r')
    data = myFile.read()
    words = data.split(" ")
    write(data)

def write(data):
	i=0
	j=0
	k=0
	kronus0_start = time.time()
	while i < 10000:
	        i += 1
	        fileName = "kronus0.txt"
	        outFile = open(fileName, 'a+')
	        outFile.write(data)
	outFile.close()
	kronus0_end = time.time()
	kronus1_start = time.time()
	while j < 100000:
	        j += 1
	        fileName = "kronus1.txt"
	        outFile = open(fileName, 'a+')
	        outFile.write(data)
	outFile.close()
	kronus1_end = time.time()
	kronus2_start = time.time()
	while k < 1000000:
		k += 1
		fileName = "kronus2.txt"
		outFile = open(fileName, 'a+')
		outFile.write(data)
	outFile.close()
	kronus2_end = time.time()
	printRes(kronus0_start, kronus0_end, kronus1_start, kronus1_end, kronus2_start, kronus2_end)

def printRes(kronus0_start, kronus0_end, kronus1_start, kronus1_end, kronus2_start, kronus2_end):
	print("--- Kronus0 start %s seconds ---" % (kronus0_start))
	print("--- Kronus0 end %s seconds ---" % (kronus0_end))
	print("--- Kronus0 time lapse %s seconds ---" % (kronus0_end - kronus0_start))
	print("--- Kronus1 start %s seconds ---" % (kronus1_start))
	print("--- Kronus1 end %s seconds ---" % (kronus1_end))
	print("--- Kronus1 time lapse %s seconds ---" % (kronus1_end - kronus1_start))
	print("--- Kronus2 start %s seconds ---" % (kronus2_start))
	print("--- Kronus2 end %s seconds ---" % (kronus2_end))
	print("--- Kronus2 time lapse %s seconds ---" % (kronus2_end - kronus2_start))
	
	
main()





