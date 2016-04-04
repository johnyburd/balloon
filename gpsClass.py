import gps

class gpsClass:
    def __init__(self, host, port):
        self.session = gps.gps(host,port)
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
        return self.report("lat")

    def getLon(self):
        return self.report("lon")

    def getSpeed(self):
        return self.report("speed")

    def getAlt(self):
        return self.report("alt")

    def getClimb(self):
        return self.report("climb")

    def getTime(self):
        return self.report("time")
