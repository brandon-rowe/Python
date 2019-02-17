def main():
    # Program to multiply two matrices using list comprehension

    # 5x3 matrix
    X = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15]]

    # 3x5 matrix
    Y = [[row[i] for row in X] for i in range(3)]

    # result is 3x4
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

    for r in result:
       print(r)
main()
