__author__ = 'pi'
#This file exposes various LED control functions

import time
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT) #Red
    GPIO.setup(13, GPIO.OUT) #Green
    GPIO.setup(15, GPIO.OUT) #Blue

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
    time.sleep(5)
    GPIO.cleanup()


def cleanup():
    GPIO.cleanup()

#http://blog.oscarliang.net/raspberry-pi-and-arduino-connected-serial-gpio/