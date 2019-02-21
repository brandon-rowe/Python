#output the product of two maticies A*A
#where A is the transpose of A
#this is a 5X3 matrix
#Transpose - cause (two or more things) to change places with each other.
def main():
    X = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15]]

    Y = []
    for i in range(3):
        Y.append([row[i] for row in X])

    result =[]

    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]

    for r in result:
       print(r)

main()