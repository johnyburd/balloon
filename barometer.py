import Adafruit_BMP.BMP085 as BMP085

class Barometer(object):
    def __init__(self):
        print "hello"
        self.sensor = BMP085.BMP085()
        print self.sensor

    def getTempC(self):
        return "{0:0.2f}".format(self.sensor.read_temperature())
    def getTempF(self):
        return "{0:0.2f}".format((self.sensor.read_temperature()*9)/5+32)
    def getPressure(self):
        #Pa
        return self.sensor.read_pressure()
    def getAlt(self):
        return self.sensor.read_altitude()
    def getSeaLevelPressure(self):
        return self.sensor.read_sealevel_pressure()
