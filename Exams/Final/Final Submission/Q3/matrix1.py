#nested list comprehension
def main():
    X = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    Y = [[row[i] for row in X] for i in range(3)] #transposed list
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    for r in result:
       print(r)
main()
