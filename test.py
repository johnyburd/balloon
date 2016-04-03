import gps
from Webcam import Webcam
import barometer
import cellDongle 
import time

def main():
    print("initializing balloon equipment")
    print("3g... " + cellDongle.status())
    print("GPS... ")
    gps1 = gpsClass("localhost","99")
    print("Webcam 1...")
    cam1 = Webcam("/dev/video1","1600x1200")
    print(cam1.status())
    print("Webcam 2...")
    cam2 = Webcam("/dev/video0","640x480")
    print(cam2.status())
    print("Barometer... " + barometer.status())

    print cam1.take_pic()
    print cam2.take_pic()

    print ("lat: "+gps1.getLat())
    print("lon: "+ gps1.getLon())
    print("speed: " + gps1.getSpeed())
    print("alt: " + gps1.getAlt())
    print("climb: " + gps1.getClimb())
    print("time: " + gps1.getTime())



if __name__ == "__main__":
    main()
