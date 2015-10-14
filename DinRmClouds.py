__author__ = 'madsens'
import Lights
import Logging
import os
import datetime
import time
import AudioRandomizer

Lights.setup()
previousFile = ""
lastScan = 0

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        Lights.cleanup()
        break  # stops the loop
    else :
        #Trigger GPIO Pins. Lightning sticks on 13
        Lights.activatePins([13])
        print "Activate Pins\n"

        #Log Activation of PI
        Logging.LogAccess(n)

        #If Between the hours of 630-10PM, Play Rumble
        now = datetime.datetime.now()
        now_time = now.time()
        if time(17,30) <= now.time() <= time(21,00):
            if currentScan - lastScan > 15:
                #Play Soft Thunder
                print "It is Between 630 and 10 and NOT within activation Lockout. " \
                      "Play the Dinnertime Rumble of thunder.\n"
                os.system('mpg321 Assets/CreepyLaugh.mp3 &' )
                lastScan = currentScan
            else:
                print "It is between 630 and 10 and within the activation Lockout. " \
                      "Do not play Dinnertime rumble of thunder. "
        else:
            #Else, Play Loud thunder if not in timeout. If IN timeout, play soft dinner thunder
            if currentScan - lastScan > 15:
                print "It is outside of Dinner Hours and NOT within activation Lockout. Play a random thunder crash."
                # Play Random Thunder file
                previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)
            else:
                #Play Soft Thunder
                print "It is outside of Dinner Hours and within the activation Lockout. Do not play audio file."
                os.system('mpg321 Assets/CreepyLaugh.mp3 &' )