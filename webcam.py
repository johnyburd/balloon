import os
import picamera
import time

class Webcam:
    def __init__(self, dev, rez):
        self.picam = False
        self.device = dev

        if dev == 'picamera':
            self.picam = True
            self.camera = picamera.PiCamera()
            self.camera.resolution = (1920, 1080)

        self.resolution = rez

    def take_pic(self):
        try:
            if self.picam:
                self.camera.capture(time.strftime("%d_%H:%M:%S") + ".jpg")
            else:
                retval = os.system("fswebcam --no-banner --quiet -S 2 -d " + self.device + " -r " + self.resolution + " /home/pi/balloon/$(date +\"%d_%H:%M:%S\").jpg")
            return retval
        except:
            print("webcam " + str(self.device) + " error")

    def status(self):
        if self.picam:
            return("not sure")
        else:
            retval = os.system("ls " + self.device)
            if retval == 0:
                return("detected")
            return("not detected")

