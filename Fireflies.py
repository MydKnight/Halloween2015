__author__ = 'madsens'

import Lights
import time
import Logging
import os
# This code runs the fireflies gag

lastScan = 0

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        break  # stops the loop
    else :
        #Trigger GPIO Pins. Do mod3 on the card. If 0, X and Y, if 1 trigger X, if 2 trigger Y.
        if n%3 == 0:
            Lights.activatePins(11, 13)
        elif n%3 == 1:
            Lights.activatePins(11)
        elif n%3 == 2:
            Lights.activatePins(13)
        print "Modulo: ",n%3

        #If not within timeout window, play sound file
        if currentScan - lastScan < 15:
            print "Elapsed Time: ", currentScan - lastScan
        else:
            os.system('mpg321 CreepyLaugh.mp3 &')

        #Finally Log Activation of PI
        Logging.LogAccess(n)




