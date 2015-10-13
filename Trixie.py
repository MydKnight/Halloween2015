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
        print "Current Scan: " + currentScan + "\n"
        print "Last Scan: " + currentScan + "\n"
        #If not within timeout window, play sound file
        if currentScan - lastScan < 15:
            print "Elapsed Time: ", currentScan - lastScan
        else:
            #Log Activation of PI
            Logging.LogAccess(n)

            #Trigger GPIO Pins. Trixie just uses pin 13
            Lights.activatePins([13])

            previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)

            lastScan = currentScan