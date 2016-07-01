
from gpsClass import GpsPoller
from webcam import Webcam
from barometer import Barometer
from cellDongle import CellDongle
import time
import sys

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
        for i in xrange(3):
            record_gps(gpsp)

            record_barometer(bar1)

        cam1.take_pic()
        cam2.take_pic()


    
