__author__ = 'madsens'
import Logging
import os
import time
import random
import signal
from DmxPy import DmxPy

dmx = DmxPy('/dev/ttyUSB0')
TIMEOUT = 30
previousFile = 1

def interrupted(signum, frame):
    global previousFile
    global dmx

    print 'Nine minutes have passed. Playing files'
    rnd = random.randint(1,4)
    if rnd == 4:
        # Do Pumpkin Tree
        # Play Glassando Audio

        # Make Lightshow happen

        print "pumpkin tree stuff here"
    else:
        # Do Pumpkin Talk
        # Play next pumpkin file.
        os.system('mpg321 Assets/PumpkinAudio/%i.mp3' %previousFile )
        if previousFile == 22:
            previousFile = 1
        else:
            previousFile += 1
    signal.alarm(TIMEOUT)

def input():
    global previousFile
    global dmx

    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        print 'PKill scanned. Aborting Script.'
        return False
    else :
        #Log Activation of PI - Disable for now
        #Logging.LogAccess(n)

        rnd = random.randint(1,4)
        if rnd == 4:
            # Do Pumpkin Tree
            # Play Glassando Audio
            os.system('mpg321 Assets/PumpkinAudio/glissando.mp3')
            # Make Lightshow happen
            for x in range(0, 50):
                rndPump = random.randint(1,2)
                dmx.setChannel(rndPump, 100)
                dmx.render()
                time.sleep(.5)
                dmx.blackout()
                dmx.render()
            print "pumpkin tree stuff here"
        else:
            # Do Pumpkin Talk
            # Play next pumpkin file.
            os.system('mpg321 Assets/PumpkinAudio/%i.mp3' %previousFile)
            if previousFile == 22:
                previousFile = 1
            else:
                previousFile += 1

signal.signal(signal.SIGALRM, interrupted)

while True:
    #set alarm
    print "Setting alarm to: ", TIMEOUT
    signal.alarm(TIMEOUT)
    s = input()
    if s == False:
        break
    #disable the alarm after success
    signal.alarm(0)