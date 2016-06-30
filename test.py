from gpsClass import GpsPoller
from webcam import Webcam
from barometer import Barometer
from cellDongle import CellDongle
import time
import sys
# -*- coding: utf-8 -*-


#sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock -S 99

def main():
    print("Initializing Equipment")

    print("3g... ")
    data = CellDongle()
    print("Status: " + data.detected())
    print("Attempting connection...")
    #print(data.connect())
    print("Testing status...")
   # print(data.status())
    print("Disconnecting...")
    #print(data.disconnect())

    print("GPS... ")
    print("Starting daemon...") ## actually happens in gpsClass.py
    gpsp = GpsPoller("localhost","99", "/dev/ttyUSBgps")
    gpsp.start()
    print("LifeCam...")
   # print '/dev/v4l/by-id/usb-Microsoft_Microsoft_LifeCam_NX-6000-video-index0'.encode('utf-8')
    cam1 = Webcam('/dev/v4l/by-id/usb-Microsoft_Microsoft*_LifeCam_NX-6000-video-index0',"1600x1200")
    #print(cam1.status())
    print("iSight..")
    cam2 = Webcam("/dev/v4l/by-id/usb-Micron_Built-in_iSight-video-index0","352x288")
    print("Barometer... ")
    bar1 = Barometer()

    cam1.take_pic()
    cam2.take_pic()

    print("camera2 status: " + cam2.status())
    #print(gps1.getLat())

    for i in xrange(3):
        try:
            print gpsp.getDMS()
            #print gpsd.utc, gpsd.fix.time
        # print("speed: {0:0.2f} m/s".format(gps1.getSpeed()))
        # print("alt: {0:0.2f} m").format(gps1.getAlt())
        # print("climb: {0:0.2f} m/s".format(gps1.getClimb()))
        # print("time: {0} ".format(gps1.getTime()))
        except NameError:
            print("GPS missing connection")
            gpsp.update_daemon()

        except:
            e = sys.exc_info()[0]
            print("GPS Error:")
            print e
            gpsp.update_daemon()

    try:
        print("temp *C " + bar1.getTempC())
        print("temp *F " + bar1.getTempF())
        print("pressure alt: {0:0.2f} m".format(bar1.getAlt()))
        print("pressure: {0:0.2f} pa".format(bar1.getPressure()))
  #  print("sea level pressure " + bar1.getSeaLevelPressure())
    except:
        e = sys.exc_info()[0]
        print("Barometer Error: ")
        print e

    gpsp.running = False
    gpsp.join()



if __name__ == "__main__":
    main()
