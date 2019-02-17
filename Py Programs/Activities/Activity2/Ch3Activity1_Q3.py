import math
def main():
    r = eval(input("Please enter the radius of a sphere: "))
    v = (4/3) * math.pi * math.pow(r, 3)
    a = 4 * math.pi * math.pow(r, 2)
    print("You entered a radius of",r)
    print("The volume of the sphere is",v)
    print("The area of the sphere is",a)
main()
