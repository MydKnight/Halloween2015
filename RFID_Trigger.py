__author__ = 'shilohmadsen'
# This code will have the main listener app. It will wait for a "keyboard" input and when recieved, will execute the code
# contained within the function. Individual tasks, such as play video, actuate motors or light up leds will be their own
# function files included in the code. This will allow us to have modular code to use for pis doing only what it needs to do.

import Lights
import Movies
import time

Movies.StartLoop('/home/pi/Halloween2015/Assets/VideoLoop')
Lights.setup()

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    Lights.showColor("gold")
    n = raw_input("Scanned ID: ")
    if n == "0001603911":
        Movies.StopLoop()
        Lights.cleanup()
        break  # stops the loop
    else :
        #Insert various function calls to run files etc.
        Lights.showColor("red")
        time.sleep(2)
        Movies.PlayMovie()
