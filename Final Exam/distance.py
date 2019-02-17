import math

def main():
    lat1 = float(input("Please enter the lattitude of first location. "))
    lon1 = float(input("Please enter the longitude of first location. "))
    lat2 = float(input("Please enter the lattitude of second location. "))
    lon2 = float(input("Please enter the longitude of second location. "))
    distanceFormula(lat1, lon1, lat2, lon2)

def distanceFormula(lat1, lon1, lat2, lon2):
    R = 3,950 # Radius of earth in miles
    degLat = math.radians(lat2-lat1) # Convert degrees to radians
    degLon = math.radians(lon2-lon1)
    a = math.sin(degLat/2) * math.sin(degLat/2) + math.cos(math.radians(lat1) * math.cos(math.radians(lat2)) * math.sin(degLon/2) * math.sin(degLon/2)
    b = math.sqrt(a)
    c = math.sqrt(1-a)
    d = 2 * math.atan2(b, c)
    e = R * d
    return e

main()
