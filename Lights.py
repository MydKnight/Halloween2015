__author__ = 'pi'
#This file exposes various LED control functions

import time
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

def showColor(color):
    if color == "gold":
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        return
    elif color == "red":
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, False)
        return
    else:
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        return

def activatePins(pinArray):
    for pin in pinArray:
        GPIO.output(pin, True)
        print "Set " + str(pin) + " to On. \n"

        time.sleep(1)

        #Then set all pins back to false.
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(33, False)
        GPIO.output(35, False)
        GPIO.output(37, False)

def cleanup():
    GPIO.cleanup()

#http://blog.oscarliang.net/raspberry-pi-and-arduino-connected-serial-gpio/