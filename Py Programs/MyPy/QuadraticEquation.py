import math
import cmath

def main():
        a = float(input("Please enter a value for a: "))
        b = float(input("Please enter a value for b: "))
        c = float(input("Please enter a value for c: "))

        x = math.pow(b, 2)-(4*a*c)

        top1 =  (-b)-(cmath.sqrt(x))
        bottom1 = 2 * a
        ans1 = top1/bottom1
        
        top2 = (-b)+(cmath.sqrt(x))
        bottom2 = 2 * a
        ans2 = top2/bottom2

        print(ans1)
        print(ans2)
main()
