import os

class Webcam:
    def __init__(self, dev, rez):
        self.device = dev
        self.resolution = rez

    def take_pic(self):
        retval = os.system("fswebcam --no-banner -S 2 -d " + self.device + " -r " + self.resolution + " $(date +\"%d_%H:%M:%S\").jpg")
        return retval

    def status(self):
        return "good"
