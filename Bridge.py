__author__ = 'madsens'
from subprocess import Popen, PIPE
import time

while True:
    Popen(['mpg321', '/home/pi/Halloween2015/Assets/BridgeHorse.mp3', '--gain', '100'], stdout=PIPE, close_fds=True)
    print "Sleeping for 60 seconds."
    time.sleep(60)