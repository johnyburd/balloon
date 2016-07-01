
from gpsClass import GpsPoller
from webcam import Webcam
from barometer import Barometer
from cellDongle import CellDongle
import time
import sys
import time
import socket
import os

GROUND_ELEVATION = 346 #m
REMOTE_SERVER = "www.google.com"
SERVER_HOST = "johnyburd@24.158.200.117"

def main():

    print("Initializing Equipment")
    print

    print("3g... ")
    data = CellDongle()
    print("Status: " + data.detected())
    print("Attempting connection...")
    #print(data.connect())
    print("Testing status...")
   # print(data.status())
    print("Disconnecting...")
    #print(data.disconnect())
    print

    print("GPS... ")
    print("Starting daemon...") ## actually happens in gpsClass.py
    gpsp = GpsPoller("localhost","99", "/dev/ttyUSBgps")
    gpsp.start()
    print

    print("LifeCam webcam...")
   # print '/dev/v4l/by-id/usb-Microsoft_Microsoft_LifeCam_NX-6000-video-index0'.encode('utf-8')
    cam1 = Webcam('/dev/v4l/by-id/usb-Microsoft_Microsoft*_LifeCam_NX-6000-video-index0',"1600x1200")
    print("status: " + cam1.status())
    print

    print("iSight webcam..")
    cam2 = Webcam("/dev/v4l/by-id/usb-Micron_Built-in_iSight-video-index0","352x288")
    print("status: " + cam2.status())
    print

    print("Barometer... ")
    bar1 = Barometer()
    print


    while True:
        altitude = 0
        try:
            altitude = gpsp.get_altitude()
        except:
            try:
                altitude = bar1.getAlt()
            except:
                print("Neither GPS nor barometer can give altitude.  Assuming device is on the ground.")

        for i in xrange(3):
            record_gps(gpsp)
            print

            record_barometer(bar1)
            print

            time.sleep(3)

        print("Webcam 1 picture...")
        cam1.take_pic()
        print("Webcam 2 picture...")
        cam2.take_pic()
        print

        time.sleep(5)

        if (altitude < 3048 + GROUND_ELEVATION): #10000ft in m
            if (not is_connected()):
               try:
                    data.connect()
                    print("Connection successful: " + str(is_connected()))
                    print(str(data.ip_addr()))
               except:
                    print("Could not connect because of an error")
        if (is_connected()):
            try:
                retval = os.system("scp /home/pi/balloon/*.txt " + SERVER_HOST + ":.")
                if retval == 0:
                    print("Copied txt files")
                else:
                    print("Error copying files")
            except:
                print("Double error copying files")



def is_connected():
    try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
        host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
        return False


def record_gps(gpsp):

    try:
        print gpsp.getDMS()
        print gpsp.test()
    except NameError:
        print("GPS missing connection")
        gpsp.update_daemon()

    except:
        e = sys.exc_info()[0]
        print("GPS Error:")
        print e
        gpsp.update_daemon()

def record_barometer(bar1):

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
if __name__ == "__main__":
    main()
