import os

class Webcam:
    def __init__(self, dev, rez):
        self.device = dev
        self.resolution = rez

    def take_pic(self):
        try:
            retval = os.system("fswebcam --no-banner -S 2 -d " + self.device + " -r " + self.resolution + " /home/pi/balloon/$(date +\"%d_%H:%M:%S\").jpg")
            return retval
        except:
            print("webcam " + str(self.device) + " error")

    def status(self):
        retval = os.system("ls " + self.device)
        if retval == 0:
            return("detected")
        return("not detected")

