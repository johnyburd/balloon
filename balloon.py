
from gpsClass import GpsPoller
from webcam import Webcam
from barometer import Barometer
from cellDongle import CellDongle
import time
import sys
import time
import socket
import os
import math
import subprocess

GROUND_ELEVATION = 346 #m
REMOTE_SERVER = "www.google.com"
SERVER_HOST = "johnyburd@24.158.201.145"

def main():

    print("Initializing Equipment")
    print

    print("3g... ")
    data = CellDongle()
    print("Status: " + data.detected())
    print

    print("GPS... ")
    print("Starting daemon...") ## actually happens in gpsClass.py
    gpsp = GpsPoller("localhost","99", "/dev/ttyUSBgps")
    gpsp.start()
    print

    print("PiCamera webcam...")
    cam1 = Webcam('picamera',"1920x1080")
    print("status: " + cam1.status())
    print

    print("Generic webcam..")

    cam2 = Webcam('/dev/v4l/by-id/usb-Generic_FULL_HD_1080P_Webcam_200901010001-video-index0',"1920x1080")
    print("status: " + cam2.status())
    print

    print("Barometer... ")
    bar1 = Barometer()
    print
    notTriggered = True


    while True:
        altitude = 0
        try:
            altitude = gpsp.get_altitude()
        except:
            try:
                altitude = bar1.getAlt()
            except:
                print("Neither GPS nor barometer can give altitude.  Assuming device is on the ground.")
        try:
            if math.isnan(altitude):
                altitude = int(0)
        except:
            pass
        print("altitude: " + str(altitude))

        for i in xrange(3):
            record_gps(gpsp)
            print

            record_barometer(bar1)
            print

            time.sleep(3)

        print("Webcam 1 picture...")
        #cam1.take_pic()
        print(cam1.status())
        print("Webcam 2 picture...")
        #cam2.take_pic()
        print(cam2.status())

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
            print("Connected to the internet")
            print
            try:
                retval = os.system("scp /home/pi/balloon/*.txt " + SERVER_HOST + ":.")
                if retval == 0:
                    print("Copied txt files")
                else:
                    print("Error copying files")
            except:
                print("Double error copying files")

            if (altitude < 150 + GROUND_ELEVATION and notTriggered):
                try:
                    print("Attempting to beam home the first few pictures")
                    retval = os.system("scp /home/pi/balloon/*.jpg " + SERVER_HOST + ":. && mv /home/pi/balloon/*jpg /home/pi")
                except:
                    print("uh oh, something went wrong already?")
            else:
                notTriggered = False



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
