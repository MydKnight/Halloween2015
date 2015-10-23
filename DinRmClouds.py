__author__ = 'madsens'
import Lights
import Logging
import os
import datetime
import time
import AudioRandomizer
import signal

#Lights.setup()
previousFile = ""
lastScan = 0

TIMEOUT = 30

def interrupted(signum, frame):
    #do stuff when read times out
    print 'Interrupting to do other things'

signal.signal(signal.SIGALRM, interrupted)

def input():
    global lastScan
    global previousFile

    try:
        print 'You have 30 seconds to type in your stuff....'
        n = raw_input("Scanned ID: ")
        currentScan = time.time()
        if n == "0001603911":
            Lights.cleanup()
            return False
        else :
            #Trigger GPIO Pins. Lightning sticks on 13
            Lights.activatePins([13])
            print "Activate Pins\n"

            #Log Activation of PI
            Logging.LogAccess(n)

            #If Between the hours of 630-10PM, Play Rumble
            now = datetime.datetime.now()
            now_time = now.time()
            print datetime.time(17,30)
            if datetime.time(17,30) <= now.time() <= datetime.time(21,00):
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
                    lastScan = currentScan
                    # Play Random Thunder file
                    previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)
                else:
                    #Play Soft Thunder
                    print "It is outside of Dinner Hours and within the activation Lockout. Play Soft Thunder."
                    os.system('mpg321 Assets/CreepyLaugh.mp3 &' )
        return
    except:
        #timeout
        return

while True:
    #set alarm
    signal.alarm(TIMEOUT)
    s = input()
    if s == False:
        break
    #disable the alarm after success
    signal.alarm(0)



''' Commenting out the whole block so i can test timout
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
        print datetime.time(17,30)
        if datetime.time(17,30) <= now.time() <= datetime.time(21,00):
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
                lastScan = currentScan
                # Play Random Thunder file
                previousFile = AudioRandomizer.PlayRandomAudio("Assets/Trixie/", previousFile)
            else:
                #Play Soft Thunder
                print "It is outside of Dinner Hours and within the activation Lockout. Play Soft Thunder."
                os.system('mpg321 Assets/CreepyLaugh.mp3 &' )'''