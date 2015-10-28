__author__ = 'madsens'

import Lights
import time
import Logging
from subprocess import Popen, PIPE
import os
# This code runs the fireflies gag

lastScan = 0
Lights.setup()
previousFile = ""
Popen(['mpg321', '/home/pi/Halloween2015/Assets/Crickets.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)

#Turn the reader back on.
os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        Lights.cleanup()
        break  # stops the loop
    else :
        #Turn off the reader until function finishes.
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        Popen(['mpg321', '/home/pi/Halloween2015/Assets/CreepyLaugh.mp3'], stdout=PIPE, close_fds=True)
        #Log Activation of PI
        #Logging.LogAccess(n)

        #Trigger GPIO Pins. Do mod3 on the card. If 0, X and Y, if 1 trigger X, if 2 trigger Y.
        num=int(n)
        if num%3 == 0:
            Lights.activatePins([33])
            time.sleep(9)
        elif num%3 == 1:
            Lights.activatePins([35])
            time.sleep(9)
        elif num%3 == 2:
            Lights.activatePins([37])
            time.sleep(9)
        print "Modulo: ",num%3

        lastScan = currentScan

        #Turn the reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")