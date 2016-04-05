from gpsClass import GpsClass
from Webcam import Webcam
from barometer import Barometer
import cellDongle 
import time

def main():
    print("initializing balloon equipment")
#    print("3g... " + cellDongle.status())
    print("GPS... ")
    gps1 = GpsClass("localhost","99")
    print("Webcam 1...")
    cam1 = Webcam("/dev/video1","1600x1200")
    #print(cam1.status())
    print("Webcam 2...")
    cam2 = Webcam("/dev/video0","640x480")
    print(cam2.status())
    print("Barometer... ")
    bar1 = Barometer()

 #   print cam1.take_pic()
 #   print cam2.take_pic()

    #print(gps1.getLat())
    print "dms"
    print gps1.getDMS()
    print gps1.getTime()
    #print(gps1.getLon())
    print("speed: {0:0.2f} m/s".format(gps1.getSpeed()))
    print("alt: {0:0.2f} m").format(gps1.getAlt())
    print("climb: {0:0.2f} m/s".format(gps1.getClimb()))
    print("time: {0} ".format(gps1.getTime()))

    print("temp *C " + bar1.getTempC())
    print("temp *F " + bar1.getTempF())
    print("pressure alt: {0:0.2f} m".format(bar1.getAlt()))
    print("pressure: {0:0.2f} pa".format(bar1.getPressure()))
  #  print("sea level pressure " + bar1.getSeaLevelPressure())



if __name__ == "__main__":
    main()
