__author__ = 'madsens'
from subprocess import Popen, PIPE
import time
import random

while True:
    rnd = random.randint(15,600)
    Popen(['mpg321', '/home/pi/Halloween2015/Assets/BridgeHorse.mp3', '--gain', '100'], stdout=PIPE, close_fds=True)
    print "Sleeping for %i seconds." %rnd
    time.sleep(rnd)