#!/usr/bin/python
import serial
#import syslog
import time

#The following line is for serial over GPIO
port = 'COM3' 

ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

ard.flush()
global op
op=0
while op!='q':
    op=input("Enter value to send (q to exit): ")
    print ("Value sent: ")
    print (op)
    ard.write(op.encode())

else:
    exit()
exit()
