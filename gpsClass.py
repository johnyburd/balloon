#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self, h, p, d):
    self.host = h
    self.port = p
    self.device = d

    self.update_daemon()

    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    #gpsd = gps.gps("localhost", "99")
    gpsd = gps(self.host, self.port, mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while self.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


  def getDMS(self):
    lt = gpsd.fix.latitude
    ln = gpsd.fix.longitude

    lat = self.decToDMS(lt)
    lon = self.decToDMS(ln)

    latHem = 'N'
    lonHem = 'E'

    if not lat[0]:
      latHem = 'S'
    if not lon[0]:
      lonHem = 'W'

    return "{0:d}".format(lat[1]) + " " + str(lat[2]) + "' {0:0.3f}\"".format(lat[3]) + latHem + " " + str(lon[1]) + " " + str(lon[2]) + "' {0:0.3f}\"".format(lon[3]) + lonHem


  def decToDMS(self, dec):
    pos = True
    if dec < 0:
      dec = abs(dec)
      pos = False

    degrees = int(math.floor(dec))
    #print degrees
    temp = dec % 1
    temp *= 60
    minutes = int(math.floor(temp))
    temp %= 1
    seconds = temp * 60

    return [pos,degrees,minutes,seconds]

  def update_daemon(self): # this function should allow the program to repair itsself if the devices get switched out from underneath it
    return os.system("sudo gpsd " + self.device + " -F /var/run/gpsd.sock -S 99")
  def get_altitude(self):
    return gpsd.fix.altitude

  def test(self):

    print ' GPS reading'
    print '----------------------------------------'
    print 'latitude    ' , gpsd.fix.latitude
    print 'longitude   ' , gpsd.fix.longitude
    print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
    print 'altitude (m)' , gpsd.fix.altitude
    print 'eps         ' , gpsd.fix.eps
    print 'epx         ' , gpsd.fix.epx
    print 'epv         ' , gpsd.fix.epv
    print 'ept         ' , gpsd.fix.ept
    print 'speed (m/s) ' , gpsd.fix.speed
    print 'climb       ' , gpsd.fix.climb
    print 'track       ' , gpsd.fix.track
    print 'mode        ' , gpsd.fix.mode
    print
    print 'sats        ' , gpsd.satellites
