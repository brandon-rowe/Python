# String Counter
def main():
    calx = float(input("Please enter a numerator: "))
    caly = float(input("Please enter a denominator: "))
    calDif = calx / caly
    myFile = open("numFile.txt",'r')
    data = myFile.read()
    nums = data.split(" ")
    total = 0
    avg = 0
    for ch in nums:
        num = int(ch)
        total += num
        avg = total / len(nums)
    lenNums = len(nums)
    print()
    avgD = float(avg)
    print("The sum is:",total)
    print("Total numbers:",lenNums)
    print("The average is ",avgD)
    print("Calculations on your digits: ", calDif)
    myFile.close()
main()
