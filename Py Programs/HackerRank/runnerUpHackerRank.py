#Take in a value N for the size of the array
#Take input values for the array
#Determine the runner-up. Same values counted
#As 1. [2, 3, 6, 6, 5] should show 5 as output
#for runnerup.
import os

def main():
    n = int(input())
    arr = map(int, input().split())
    max = -100
    lmax = -100
    a = list(arr)
    
    for x in a:
        if (x>max):
            max = x
    for x in range(n):
        for x in a:
            if (x==max):
                a.remove(x)      
    for x in range(n):
        for x in a:
            if (x>lmax):
                lmax = x
    print(lmax)
main()
