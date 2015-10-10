__author__ = 'madsens'

import Lights
import time
import Logging
import os
# This code runs the fireflies gag

lastScan = 0
Lights.setup()

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        break  # stops the loop
    else :
        #If not within timeout window, play sound file
        if currentScan - lastScan < 15:
            print "Elapsed Time: ", currentScan - lastScan
        else:
            os.system('mpg321 Assets/CreepyLaugh.mp3 &')

        #Finally Log Activation of PI
        Logging.LogAccess(n)

        #Trigger GPIO Pins. Do mod3 on the card. If 0, X and Y, if 1 trigger X, if 2 trigger Y.
        num=int(n)
        if num%3 == 0:
            Lights.showColor("red")
        elif num%3 == 1:
            Lights.activatePins([11])
        elif num%3 == 2:
            Lights.activatePins([13])
        print "Modulo: ",num%3




