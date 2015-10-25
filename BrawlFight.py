__author__ = 'madsens'
import Lights
#import Logging
import Movies
import time

Lights.setup()
Movies.StartLoop('/home/pi/Halloween2015/Assets/BrawlFight')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        print "You typed: ", n
        #Log Activation of PI - Disabled until we're configured on the castle network
        #Logging.LogAccess(n)

        #Play Furnace Video - Test
        Movies.PlayMovie()

        #Wait until the Air Cannon should fire
        time.sleep(8)

        #Trigger GPIO Pins. Air Cannon on 13
        Lights.activatePins([13])