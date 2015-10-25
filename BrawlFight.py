__author__ = 'madsens'
#import Logging
import Movies
import time
import KeyboardLocker

#Movies.StartLoop('/home/pi/Halloween2015/Assets/BrawlFight')
kl = KeyboardLocker.KeyboardLocker(serio=0)
device = kl.description()
print "We got a lock on", device

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        #Movies.StopLoop()
        break  # stops the loop
    else :
        print "You typed: ", n
        kl.turn_off()
        #Log Activation of PI - Disabled until we're configured on the castle network
        #Logging.LogAccess(n)

        #Play Furnace Video - Test
        #Movies.PlayMovie()

        #Wait until Video finishes
        time.sleep(20)
        kl.turn_on()
