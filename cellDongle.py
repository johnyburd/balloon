import subprocess
import os

class CellDongle:
    def __init__(self):
        self.usbid = "12d1:1436"

    def detected(self):
        retval = os.system("lsusb | grep " + self.usbid)
        if retval == 0:
            return("detected")
        return ("not detected")
    def connect(self):
        return subprocess.check_output(["sudo", "sakis3g", "connect"])
    def disconnect(self):
        return subprocess.check_output(["sudo", "sakis3g", "disconnect"])
    def status(self):
        return subprocess.check_output(["sudo", "sakis3g", "status"])
    def ip_addr(self):
        return subprocess.check_output(["ip", "addr"])
