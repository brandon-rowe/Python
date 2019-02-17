# Two Dimensional Array

def main():
    x = int(input("Please enter a value for x: "))
    y = int(input("Please enter a value for y: "))
    ijrray = [[0 for col in range(y) ] for row in range(x)]

    for row in range(x):
        for col in range(y):
            ijrray[row][col] = row * col

    print(ijrray)

main()
