# Chapter 8
# Activiy 1
# Question 1
def process(sample):
    count = 0
    new =[]
    same = []
    for str in sample:
        if len(str) > 2:
            new.append(str)

    for str in new:
        n = len(str)
        if str[0] == str[n-1]:
            same.append(str)
            count+=1
    for str in same:
        print(str)
    print("Result:",count)
    
def main():
    sample = ['abc','xyz','a','en','aba','1221','11','333']
    process(sample)

main()


#def main():
#    list1 = ['1','abc','xyz','aba','1221','1']
#    matrix1 = [[1,2],[3,4]]
#    i = 1
#    e = 0
#    for str in list1:
#        n = len(str)
#        if n >= 2:
#            print(i, str)
#            i += 1
            #for ch in str:
                #while i = 0 and i = (n - 1):
                    #e += 1
                    #print(e)
#    for list in matrix1:
#        print(list)
#    print(matrix1)

#main()
