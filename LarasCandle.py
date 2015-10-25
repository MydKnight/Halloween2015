__author__ = 'madsens'

import Lights
import os
import time

Lights.setup()

os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    if n == "0001603911":
        break  # stops the loop
    else :
        #Disable RFID
        os.system("/home/pi/Halloween2015/Scripts/disableRFID.sh")

        #Trigger GPIO Pins. This uses a Relay, so we need to actually call OFF to turn it on...
        Lights.off([13])

        time.sleep(3)

        #Candle GPIO "off"
        Lights.on([13])

        #Log Activation of PI
        #Logging.LogAudioAccess(n, previousFile)

        #Reenable RFID
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")
