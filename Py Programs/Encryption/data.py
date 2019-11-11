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
	txt0_start = time.time()
	fileName = "txt0.txt"
	outFile = open(fileName, 'a+')
	while i < 10000:
		i += 1
		outFile.write(data)
	outFile.close()
	txt0_end = time.time()
	txt1_start = time.time()
	fileName = "txt1.txt"
	outFile = open(fileName, 'a+')
	while j < 100000:
		j += 1
		outFile.write(data)
		if j == 25000:
			print("25000")
		elif j == 50000:
			print("50000")
		elif j == 75000:
			print("75000")
	outFile.close()
	txt1_end = time.time()
	txt2_start = time.time()
	fileName = "txt2.txt"
	outFile = open(fileName, 'a+')
	while k < 500000:
		k += 1
		outFile.write(data)
		if k == 50000:
			print("50000")
		elif k == 100000:
			print("100000")
		elif k == 250000:
			print("250000")
		elif k == 350000:
			print("350000")
	outFile.close()
	txt2_end = time.time()
	printRes(txt0_start, txt0_end, txt1_start, txt1_end, txt2_start, txt2_end)
	

def printRes(txt0_start, txt0_end, txt1_start, txt1_end, txt2_start, txt2_end):
	print("--- txt0 start %s seconds ---" % (txt0_start))
	print("--- txt0 end %s seconds ---" % (txt0_end))
	print("--- txt0 time lapse %s seconds ---" % (txt0_end - txt0_start))
	print("--- txt1 start %s seconds ---" % (txt1_start))
	print("--- txt1 end %s seconds ---" % (txt1_end))
	print("--- txt1 time lapse %s seconds ---" % (txt1_end - txt1_start))
	print("--- txt2 start %s seconds ---" % (txt2_start))
	print("--- txt2 end %s seconds ---" % (txt2_end))
	print("--- txt2 time lapse %s seconds ---" % (txt2_end - txt2_start))
	
	
main()





