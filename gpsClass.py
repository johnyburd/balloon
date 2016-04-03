import gps

class gpsClass:
    def __init__(self, ip, port):
        self.session = gps.gps(ip,port)
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def report(self, reportType):
        for i in xrange(10):
            try:
                report = self.session.next()
                if report['class'] == 'TPV':
                    if hasattr(report, reportType):
                        return report.reportType
            except:
                return 1

    def getLat(self):
        return report(lat)

    def getLon(self):
        return report(lon)

    def getSpeed(self):
        return report(speed)

    def getAlt(self):
        return report(alt)

    def getClimb(self):
        return report(climb)

    def getTime(self):
        return report(time)
