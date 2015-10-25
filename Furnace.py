__author__ = 'madsens'
import Lights
#import Logging
import Movies
import os
import time

#Turn reader back on.
os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

Lights.setup2()
Movies.StartLoop('/home/pi/Halloween2015/Assets/Furnace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    #Lights.activatePins([11])
    if n == "0001603911":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        #Log Activation of PI
        #Logging.LogAccess(n)

        #Trigger GPIO Pins. 13 is Red
        Lights.activatePins([13])

        #Turn off the reader until function finishes.
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        #Play Furnace Video
        Movies.PlayMovie()

        time.sleep(20)

        Movies.PlayLoop()

        #Turn reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")