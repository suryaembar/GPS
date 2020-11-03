import string
import pynmea2
import urllib
import requests
#import threading
#import json
URl='https://api.thingspeak.com/update?api_key='
KEY='SFHRK7FDX3U4VWEQ'
#loop for the GPS

while 1:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    print ("get latitude n longitude")
    if newdata[0:6] == '$GPGGA':
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        #print (lat)
        lng = newmsg.longitude
        #print (lng)
        HEADER='&field1={}&field2={}'.format(lat,lng)
        NEW_URL= URl+KEY+HEADER
        print(NEW_URL)
        data = urllib.urlopen(NEW_URL)
        print(data)
    
time.sleep(5)
