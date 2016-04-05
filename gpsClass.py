import gps

class GpsClass:
    def __init__(self, host, port):
        #self.session = gps.gps(host,port)
        self.session = gps.gps("localhost","99")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def report(self, reportType):
        for i in xrange(10):
            try:
                report = self.session.next()
                if report['class'] == 'TPV':
                    if hasattr(report, reportType):
                        return getattr(report, reportType)
            except:
                return 1

    def getDMS(self):
        lt = self.getLat()
        ln = self.getLon()

        lat = self.decToDMS(lt)
        lon = self.decToDMS(ln)

        latHem = 'N'
        lonHem = 'E'

        if not lat[0]:
            latHem = 'S'
        if not lon[0]:
            lonHem = 'W'

        return lat[1] + "d" + lat[2] + "'{0:0.3f}\"".format(lat[3]) + latHem + " " + lon[1] + "d" + lon[2] + "'{0:0.3f}\"".format(lon[3]) + lonHem


    def decToDMS(dec):
        pos = True
        if dec < 0:
            dec = abs(dec)
            pos = False

        degrees = int(math.floor(dec))
        temp = dec % 1
        temp *= 60
        minutes = int(math.floor(temp))
        temp %= 1
        seconds = temp * 60

        return [pos,degrees,minutes,seconds]


    def getLat(self):
        return self.report("lat")

    def getLon(self):
        return self.report("lon")

    def getSpeed(self):
        return self.report('speed')

    def getAlt(self):
        return self.report("alt")

    def getClimb(self):
        return self.report("climb")

    def getTime(self):
        return self.report("time")

