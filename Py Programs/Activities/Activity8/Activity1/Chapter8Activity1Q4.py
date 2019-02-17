# Chapter 8
# Activiy 1
# Question 4
def main():
    test = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    new = [[row[i] for row in test] for i in range(3)]
    print(new)
    regularNestedLoop(test)

def regularNestedLoop(test):
    new = []
    for i in range(3):
        new.append([row[i] for row in test])
    print(new)
main()
