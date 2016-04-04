import Adafruit_BMP.BMP085 as BMP085

class barometer:
    def __init___(self):
        sensor = BMP085.BMP085()

    def getTempC(self):
        return sensor.read_temperature()
    def getTempF(self):
        return (sensor.read_temperature()*9)/5+32
    def getPressure(self):
        #Pa
        sensor.read_pressure()
    def getAlt(self):
        sensor.read_altitude()
    def getSeaLevelPressure(self):
        sensor.read_sealevel_pressure()
