__author__ = 'madsens'
import Lights
import Logging
import Movies

Lights.setup()
Movies.StartLoop()

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "0001603911":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        #Trigger GPIO Pins. Fogger on 13
        Lights.activatePins([13])

        #Play Furnace Video - Test
        Movies.PlayMovie()

        #Log Activation of PI
        Logging.LogAccess(n)
