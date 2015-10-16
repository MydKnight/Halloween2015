__author__ = 'madsens'
import Lights
import Logging
import Movies
import time

Lights.setup()
Movies.StartLoop('/home/pi/Halloween2015/Assets/VideoLoop')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "0001603911":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        #Log Activation of PI
        Logging.LogAccess(n)

        #Play Furnace Video - Test
        Movies.PlayMovie()

        #Wait until the Air Cannon should fire
        time.sleep(10)

        #Trigger GPIO Pins. Air Cannon on 13
        Lights.activatePins([13])

        #Wait for the rest of the Movie
        time.sleep(5)