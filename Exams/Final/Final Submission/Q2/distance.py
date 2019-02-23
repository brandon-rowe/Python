from math import sin, cos, sqrt, atan2, radians
def main():
    printIntro()
    d, m = getInputs()
    printResults(d, m)

def printIntro():
    print("This application will take two coordinates and return ")
    print("the distance between them in miles. ")

def getInputs():
    lat1, lon1 = input("Enter coordinate1(latt & long only): ").split()
    lat2, lon2 = input("Enter coordinate2(latt & long only): ").split()
    lat1, lon1 = [float(x) for x in [lat1, lon1]]
    lat2, lon2 = [float(x) for x in [lat2, lon2]]

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    d, m = calcDistance(lat1, lon1, lat2, lon2)
    return d, m

def calcDistance(lat1, lon1, lat2, lon2):
    R = float(6371)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    d = R * c
    m = d*0.62137
    return d, m

def printResults(d, m):
    print("Result: %s km" % (d))
    print("Result: %s miles" %(m))
    print("Rounded: %.2f km." % round(d, 2))
    print("Rounded: %.2f mi." % round(m, 2))
    print("Rounded int: %.f km." % round(d))
    print("Rounded int: %.f mi." % round(m))

main()
