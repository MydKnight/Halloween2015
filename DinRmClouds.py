__author__ = 'madsens'
import Lights
import os
import datetime
import time
import subprocess
import signal
from DmxPy import DmxPy

dmx = DmxPy('/dev/ttyUSB0')
Lights.setup()
Lights.off([37])

previousFile = ""
lastScan = 0
TIMEOUT = 540

os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')

def setHouse(intensity):
    dmx.setChannel(1, 255)
    dmx.setChannel(2, 255)
    dmx.setChannel(3, 255)
    dmx.setChannel(4, intensity)
    dmx.render()

setHouse(255)

def thunderLine(volume):
    print "Playing Thunder Line.\n"
    #Stop Playback of loop, and give it a second to clear
    subprocess.Popen(['sudo' ,'pkill', 'mpg321'])
    time.sleep(.5)
    # Play Thunder sequence
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/TriggerLightning.mp3 --gain %i -q' % volume)
    #play background loop
    os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')


def interrupted(signum, frame):
    print 'Nine minutes have passed. Playing files'
    # Relay communication is Opposite. On = Off
    Lights.off([33])
    thunderLine(100)
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
        elif n == "0003756767" or n == "0006951576" or n == "0009621329" or n == "0006968801":
            # Do Katies stuff
            # Stop Audio Loop
            subprocess.Popen(['sudo' ,'pkill', 'mpg321'])
            time.sleep(.5)

            #Trigger GPIO Pins. Lightning sticks on 33 - Relay Opposite. On=Off
            Lights.off([33])

            #Play Thunderline
            os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/HorsemanLightning.mp3 & -q')

            # After 4 secs, Dim DMX 30% Light Channels, 0% Blacklight Channels
            # Blacklight channels removed.
            time.sleep(4)
            print "House Down"
            setHouse(7)

            #Play Horseman Audio and drop heads
            time.sleep(4)

            os.system('mpg321 /home/pi/Halloween2015/Assets/HorsemanSlashes.mp3 -q &')
            time.sleep(10)

            #After 10 seconds, drop heads.
            #Trigger GPIO Pins. Head Chop on 15
            print "Drop Head"
            Lights.on([37])

            #wait an additional 11 seconds
            time.sleep(11)

            #Bring house lights back up DMX Lights 100% and stop lightning
            Lights.on([33])
            print "House Back Up"
            for x in range (20,255):
                setHouse(x)
                time.sleep(.02)
            time.sleep(30)

            #Reset Heads GPIO 11 then bring blacklight back up after 5
            print" Raising Head"
            Lights.off([37])

            #Restart Audio
            os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')
        else :
            # Do Katies stuff
            # Stop Audio Loop
            subprocess.Popen(['sudo' ,'pkill', 'mpg321'])
            time.sleep(.5)

            #Trigger GPIO Pins. Lightning sticks on 33 - Relay Opposite. On=Off
            Lights.off([33])

            #Play Thunderline
            os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/HorsemanLightning.mp3 & -q')

            # After 4 secs, Dim DMX 30% Light Channels, 0% Blacklight Channels
            # Blacklight channels removed.
            time.sleep(4)
            print "House Down"
            setHouse(7)

            #Play Horseman Audio and drop heads
            time.sleep(4)

            os.system('mpg321 /home/pi/Halloween2015/Assets/HorsemanSlashes.mp3 -q &')
            time.sleep(10)

            #After 10 seconds, drop heads.
            #Trigger GPIO Pins. Head Chop on 15
            print "Drop Head"
            Lights.on([37])

            #wait an additional 11 seconds
            time.sleep(11)

            #Bring house lights back up DMX Lights 100% and stop lightning
            Lights.on([33])
            print "House Back Up"
            for x in range (20,255):
                setHouse(x)
                time.sleep(.02)
            time.sleep(30)

            #Reset Heads GPIO 11 then bring blacklight back up after 5
            print" Raising Head"
            Lights.off([37])

            #Restart Audio
            os.system('mpg321 /home/pi/Halloween2015/Assets/Thunder/RagingWinds.mp3 --loop 0 --gain 30 -q &')
        return
    except:
        #timeout
        return

while True:
    # Reenable RFID
    os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")
    setHouse(255)
    #set alarm
    print "Setting alarm to: ", TIMEOUT
    signal.alarm(TIMEOUT)
    s = input()
    if s == False:
        break
    #disable the alarm after success
    signal.alarm(0)