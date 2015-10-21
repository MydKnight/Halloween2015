__author__ = 'madsens'
import Logging
import os
import time
import AudioRandomizer

previousFile = ""
lastScan = 0

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        break  # stops the loop
    else :
        #Log Activation of PI
        Logging.LogAccess(n)

        #Else, do X not in timeout. If IN timeout, do Y
        if currentScan - lastScan > 15:
            print "NOT within Activation Lockout"
            lastScan = currentScan
            # Play Random Thunder file
            previousFile = AudioRandomizer.PlayRandomAudio("Assets/PumpkinAudio/", previousFile)
        else:
            #Play Soft Thunder
            print "It is within the activation Lockout. Play Creepy Laugh."
            os.system('mpg321 Assets/CreepyLaugh.mp3 &' )

        #Log Activation of PI
        Logging.LogAudioAccess(n, previousFile)

# When RFID scanned

# Play Glassando Audio

# Make Lightshow happen

# Trigger talking pumkins

# Need to make it fire every X minutes anyway.
