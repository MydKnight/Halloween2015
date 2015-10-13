__author__ = 'madsens'
import Lights
import Logging
import time
from os import walk
import random
import os

lastScan = 0
Lights.setup()

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "0001603911":
        break  # stops the loop
    else :
        #Log Activation of PI
        Logging.LogAccess(n)

        #Play Random Audio File In Trixie folder.
        f = []
        for (dirpath, dirnames, filenames) in walk("Assets/Trixie"):
            f.extend(filenames)
            break
        file = random.choice(f)
        os.system('mpg321 Assets/Trixie/%s &' % file)

        #Trigger GPIO Pins. Trixie just uses pin 13
        Lights.activatePins([13])