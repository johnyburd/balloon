import math

def distanceBetweenLatLon(lat1, lon1, lat2, lon2): # haversine formular

    R = 6371000 # radius of earth in meters
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

def calcAltitude(A, B, c): # returns altitude based on ASA in radians
    C = (math.pi/2) - B - A

    a = (c * math.sin(A)) / math.sin(C)

    h = a * math.sin(B)

    return h
def calcLatLon(B, C, a, lat, lon):
    A = (math.pi/2) - B - C

    c = (a * math.sin(C)) / math.sin(A)

    loncomp = c * math.cos(math.pi)
    latcomp = c * math.sin(math.pi)

    R=6378137

    dLat = latcomp/R
    dLon = loncomp/(R*math.cos(math.pi*lat/180))

    latO = lat + dLat * 180/math.pi
    lonO = lon + dLon * 180/math.pi 
    return [latO, lonO]


def decToDMS(dec):
    pos = dec >= 0
    dec = abs(dec)

    degrees = int(math.floor(dec))
    print degrees
    temp = dec % 1
    temp *= 60
    minutes = int(math.floor(temp))
    temp %= 1
    seconds = temp * 60

    return [pos,degrees,minutes,seconds]

lat1 = 36.54752
lon1 = -82.46460
lat2 = 36.54763
lon2 = -82.46456


#distance = 1066.8
distance = distanceBetweenLatLon(lat1, lon1, lat2, lon2)
print ("distance: " + str(distance) + "m")
while True:
    A = input("elevation 1 (deg)? ")
    Ap = input("azimuth 1 (deg)? ")
    B = input("elevation 2 (deg)? ")
    Bp = input("azimuth 2 (deg)? ")

    Ap = 90 - Ap
    Bp = 90 - Bp
    print

    newlat, newlon = calcLatLon(Ap, Bp, distance, lat1, lon1)

    print("altitude: " + str(calcAltitude(math.radians(A), math.radians(B), distance)) + "m")
    print("latitude: " + str(newlat))
    print("longitude: " + str(newlon))

