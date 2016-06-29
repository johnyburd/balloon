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

lat1 = 40.7486
lon1 = -73.9864
lat2 = 40.7486
lon2 = -73.9986


#distance = 1066.8
distance = distanceBetweenLatLon(lat1, lon1, lat2, lon2)
print ("distance: " + str(distance) + "m")
while True:
    A = input("elevation 1 (deg)? ")
    Ap = input("azimuth 1 (deg)? ")
    B = input("elevation 2 (deg)? ")
    Bp = input("azimuth 2 (deg)? ")
    print()

    print("altitude: " + str(calcAltitude(math.radians(A), math.radians(B), distance)) + "m")
    print("latitude: ")
    print("longitude: ")

