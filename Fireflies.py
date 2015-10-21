__author__ = 'madsens'

import Lights
import time
import Logging
from subprocess import Popen, PIPE
import AudioRandomizer
# This code runs the fireflies gag

lastScan = 0
Lights.setup()
previousFile = ""
Popen(['mpg321', 'Assets/CreepyLaugh.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        Lights.cleanup()
        break  # stops the loop
    else :
        #If not within timeout window, play sound file
        if currentScan - lastScan < 15:
            print "Elapsed Time: ", currentScan - lastScan
            #Log Activation of PI - No Audio
            Logging.LogAccess(n)
        else:
            #kill crickets loop, play random file from Fireflies folder
            Popen(['sudo', 'pkill', 'mpg321'], stdout=PIPE, close_fds=True)
            time.sleep(1)
            previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)
            print previousFile
            #Log Activation of PI
            Logging.LogAudioAccess(n, previousFile)

        #Trigger GPIO Pins. Do mod3 on the card. If 0, X and Y, if 1 trigger X, if 2 trigger Y.
        num=int(n)
        if num%3 == 0:
            Lights.activatePins([11,13])
            time.sleep(9)
        elif num%3 == 1:
            Lights.activatePins([11])
            time.sleep(9)
        elif num%3 == 2:
            Lights.activatePins([13])
            time.sleep(9)
        print "Modulo: ",num%3

        Popen(['mpg321', 'Assets/CreepyLaugh.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)

        lastScan = currentScan



