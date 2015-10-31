__author__ = 'madsens'

import time
import os
from subprocess import Popen, PIPE
import Lights

# Setup Pins - May need to use Setup2 depending on if not reversed
Lights.setup()

# Turn the reader back on.
os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

# Loop Barn Noises
Popen(['mpg321', '/home/pi/Halloween2015/Assets/Stables/Barn.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        break  # stops the loop
    else :
        print "You typed: ", n
        #Turn off the reader until function finishes.
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        #Trigger Horse Nose - Relay so reversed
        Lights.off([37])
        time.sleep(4)
        Lights.on([37])

        #Stop Barn Noises
        Popen(['sudo' ,'pkill', 'mpg321'])
        time.sleep(1)

        #Play Horseman Audio
        Popen(['mpg321', '/home/pi/Halloween2015/Assets/Stables/Horse.mp3'], stdout=PIPE, close_fds=True)

        #Trigger Horse Eyes - Relay so reversed
        Lights.off([35])


        #Trigger Barn Door Flapping - Relay so reversed
        Lights.off([33])
        time.sleep(1)
        Lights.on([33])
        time.sleep(1)
        Lights.off([33])
        time.sleep(1)
        Lights.on([33])
        time.sleep(1)
        Lights.off([33])
        time.sleep(1)
        Lights.on([33])

        #Wait?
        time.sleep(3)

        #Trigger Horse Eyes - Relay so reversed
        Lights.on([35])

        #Restart Barn Noises
        Popen(['mpg321', '/home/pi/Halloween2015/Assets/Stables/Barn.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)

        #Turn the reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")