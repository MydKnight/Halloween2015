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
    Lights.showColor("gold")
    if n == "0001603911":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        #Turn off the reader until function finishes.
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        #Log Activation of PI
        #Logging.LogAccess(n)

        #Trigger GPIO Pins. 13 is Red
        Lights.showColor("red")
        time.sleep(2)
        Lights.showColor("none")

        #Play Furnace Video
        Movies.PlayMovie()

        time.sleep(30)

        #Turn reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")
        Lights.showColor("gold")