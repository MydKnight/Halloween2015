__author__ = 'madsens'
import Lights
import Logging
import time
import AudioRandomizer

lastScan = 0
previousFile = ""
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
            #Trigger GPIO Pins. Trixie just uses pin 13
            Lights.activatePins([13])

            previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)

            #Log Activation of PI
            Logging.LogAccess(n, previousFile)

            lastScan = currentScan