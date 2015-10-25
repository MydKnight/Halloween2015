__author__ = 'madsens'
import Lights
import os
import datetime
import time
import subprocess
import signal

Lights.setup()
previousFile = ""
lastScan = 0
TIMEOUT = 30


def thunderLine(volume):
    #Stop Playback of loop, and give it a second to clear
    subprocess.Popen(['sudo' ,'pkill', 'mpg321'])
    time.sleep(.5)
    # Play Thunder sequence
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/Lightning1.mp3 --gain %s -q &', volume)
    time.sleep(5)
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/Lightning2.mp3 --gain %s -q &', volume)
    time.sleep(5)
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/Lightning4.mp3 --gain %s -q', volume)
    time.sleep(2)
    #play background loop
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')


def interrupted(signum, frame):
    print 'Nine minutes have passed. Playing files'
    thunderLine(100)
    # Relay communication is Opposite. On = Off
    Lights.off([33])
    time.sleep(5)
    Lights.on([33])
    signal.alarm(TIMEOUT)

signal.signal(signal.SIGALRM, interrupted)


def input():
    global lastScan
    global previousFile

    try:
        print 'You have 30 seconds to type in your stuff....'
        n = raw_input("Scanned ID: ")

        #Disable RFID
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        currentScan = time.time()
        print 'Input is: ', n
        if n == "0001603911":
            print 'PKill scanned. Aborting Script.'
            Lights.cleanup()
            return False
        elif n == "1234":
            #Do Katies stuff
            #Play Thunderline
            thunderLine(100)

            #Dim DMX 30% Light Channels, 0% Blacklight Channels

            #Play Horseman Audio
            os.system('mpg321 Assets/HorsemanSlashes.mp3 -q &')
            time.sleep(6)

            #Trigger GPIO Pins. Head Chop on 15 - Temp disabling this too.
            #Lights.activatePins([15])
            time.sleep(3)

            #Bring house lights back up DMX Lights 100%
            time.sleep(30)

            #Reset Heads GPIO 11 then bring blacklight back up after 5
            #Lights.activatePins([11])
        else :
            print 'Standard Activation'

            #Trigger GPIO Pins. Lightning sticks on 33 - Relay Opposite. On=Off
            Lights.off([33])
            time.sleep(5)
            Lights.on([33])

            #Log Activation of PI - Commented out till we're on the network
            #Logging.LogAccess(n)

            #If Between the hours of 630-10PM, Play Rumble
            now = datetime.datetime.now()
            now_time = now.time()
            print datetime.time(17,30)
            if datetime.time(17,30) <= now.time() <= datetime.time(21,00):
                if currentScan - lastScan > 15:
                    #Play Soft Thunder
                    print "It is Between 630 and 10 and NOT within activation Lockout. " \
                          "Play the Dinnertime Rumble of thunder.\n"
                    thunderLine(30)
                    lastScan = currentScan
                else:
                    print "It is between 630 and 10 and within the activation Lockout. " \
                          "Do not play Dinnertime rumble of thunder. "
            else:
                #Else, Play Loud thunder outside of dinner
                print "It is outside of Dinner Hours. Play thunder."
                lastScan = currentScan
                # Play Thunder Sequence
                thunderLine(100)

        #Enable RFID
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

        return
    except:
        #timeout
        return

while True:
    #Reenable RFID
    os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")
    #play background loop
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')
    #set alarm
    print "Setting alarm to: ", TIMEOUT
    signal.alarm(TIMEOUT)
    s = input()
    if s == False:
        break
    #disable the alarm after success
    signal.alarm(0)