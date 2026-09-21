#!/usr/bin/python
import serial
#import syslog
import time

#The following line is for serial over GPIO
port = 'COM3' 

ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

ard.flushInput()
ard.flushOutput()
ard.flush()


while True:
  data_raw = ard.readline()
  #data_raw = ard.inWaiting()
  print(data_raw.decode())

    
exit()
