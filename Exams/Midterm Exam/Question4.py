# String Counter
def main():
    myFile = open("numFile.txt",'r')
    data = myFile.read()
    nums = data.split(" ")
    total = 0
    for ch in nums:
        num = int(ch)
        total += num
    lenNums = len(nums)
    print()
    print("The sum is:",total)
    print("Total numbers:",lenNums)
    print()
    myFile.close()
main()
