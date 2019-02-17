import math

class haversine:
    def __init__(self, destination1, destination2):
        lon1, lat1 = destination1
        lon2, lat2 = destination2

        R = 6371000
        phiOne = math.radians(lat1)
        phiTwo = math.radians(lat2)

        deltaPhi = math.radians(lat2-lat1)
        deltaLambda = math.radians(lon2-lon1)

        a = math.sin(deltaPhi/2.0)**2+\
            math.cos(phiOne)*math.cos(phiTwo)*\
            math.sin(deltaLambda/2.0)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

        self.meters=R*c
        self.km=self.meters/1000.0
        self.miles=self.meters*0.000621371
        self.feet=self.miles*5280

if __name__ == "__haversine__":
    main()
