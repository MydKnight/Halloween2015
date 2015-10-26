__author__ = 'madsens'
import Logging
import os
import time
import random
import signal
from DmxPy import DmxPy
from mutagen.mp3 import MP3

dmx = DmxPy('/dev/ttyUSB0')
TIMEOUT = 300
previousFile = 1
#Turn the reader back on.
os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

for x in range (1,60):
    dmx.setChannel(x, 20)
dmx.render()

def interrupted(signum, frame):
    global previousFile
    global dmx

    print 'Nine minutes have passed. Playing files'
    #Log Activation of PI - Disable for now
    #Logging.LogAccess(n)

    #Turn off the reader until function finishes.
    os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

    rnd = random.randint(1,4)
    if rnd == 4:
        # Do Pumpkin Tree
        # Play Glassando Audio
        os.system('mpg321 /home/pi/Halloween2015/Assets/PumpkinAudio/glissando.mp3 &')
        # Make Lightshow happen 1-62
        for x in range(0, 260):
            rndPump = random.randint(1,62)
            dmx.setChannel(rndPump, 255)
            dmx.render()
            time.sleep(.05)
            dmx.setChannel(rndPump, 20)
            dmx.render()
        print "pumpkin tree stuff here"
    else:
        # Do Pumpkin Talk
        # Fade Up Pumpkin Lights
        for x in range(0,255):
            dmx.setChannel(63, x)
            dmx.setChannel(64, x)
            dmx.render()
            time.sleep(.01)
        # Play next pumpkin file.
        os.system('mpg321 /home/pi/Halloween2015/Assets/PumpkinAudio/%i.mp3 &' %previousFile)
        playing = MP3("/home/pi/Halloween2015/Assets/PumpkinAudio/%i.mp3" %previousFile)
        if previousFile == 22:
            previousFile = 1
        else:
            previousFile += 1
        print "Sleeping for: %i seconds.\n" %playing.info.length
        time.sleep(playing.info.length)
        # Fade Down Pumpkin Lights
        for x in range(255,-1,-1):
            dmx.setChannel(63, x)
            dmx.setChannel(64, x)
            dmx.render()
            time.sleep(.01)

    #Turn the reader back on.
    os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")
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

        #Turn off the reader until function finishes.
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        rnd = random.randint(1,4)
        if rnd == 4:
            # Do Pumpkin Tree
            # Play Glassando Audio
            os.system('mpg321 /home/pi/Halloween2015/Assets/PumpkinAudio/glissando.mp3 &')
            # Make Lightshow happen 1-62
            for x in range(0, 260):
                rndPump = random.randint(1,62)
                dmx.setChannel(rndPump, 255)
                dmx.render()
                time.sleep(.05)
                dmx.setChannel(rndPump, 20)
                dmx.render()
            print "pumpkin tree stuff here"
        else:
            # Do Pumpkin Talk
            # Fade Up Pumpkin Lights
            for x in range(0,255):
                dmx.setChannel(63, x)
                dmx.setChannel(64, x)
                dmx.render()
                time.sleep(.01)
            # Play next pumpkin file.
            os.system('mpg321 /home/pi/Halloween2015/Assets/PumpkinAudio/%i.mp3 &' %previousFile)
            playing = MP3("/home/pi/Halloween2015/Assets/PumpkinAudio/%i.mp3" %previousFile)
            if previousFile == 22:
                previousFile = 1
            else:
                previousFile += 1
            print "Sleeping for: %i seconds.\n" %playing.info.length
            time.sleep(playing.info.length)
            # Fade Down Pumpkin Lights
            for x in range(255,-1,-1):
                dmx.setChannel(63, x)
                dmx.setChannel(64, x)
                dmx.render()
                time.sleep(.01)

        #Turn the reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

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