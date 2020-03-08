def main():
	filename = str(input("Please enter the database file"))
	thisFile = open(filename, 'r')
	data = thisFile.read()
	with open('log.txt', 'w') as f:
		f.write(data)
main()
