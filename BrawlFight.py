__author__ = 'madsens'
#import Logging
import Movies
import time

import select,sys,time,termios

Movies.StartLoop('/home/pi/Halloween2015/Assets/BrawlFight')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        break  # stops the loop
    else :
        print "You typed: ", n
        #Log Activation of PI - Disabled until we're configured on the castle network
        #Logging.LogAccess(n)

        #Play Furnace Video - Test
        Movies.PlayMovie()

        #Wait until Video finishes
        for x in range (0,20):
            time.sleep(1)
            termios.tcflush(sys.stdin,termios.TCIFLUSH)
