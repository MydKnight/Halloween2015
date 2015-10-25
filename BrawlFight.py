__author__ = 'madsens'
#import Logging
import Movies
import time
import subprocess

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

        #Turn off the reader until function finishes.
        p1 = subprocess.Popen("echo '1-1.4", stdout=subprocess.PIPE)
        p2 = subprocess.Popen('sudo tee /sys/bus/usb/drivers/unbind', stdin=p1.stdout, stdout=subprocess.PIPE)
        p2.communicate()

        #Play Furnace Video - Test
        Movies.PlayMovie()

        time.sleep(20)

        #Turn the reader back on.
        os.system("echo '1-1.4' |sudo tee /sys/bus/usb/drivers/unbind")


