__author__ = 'madsens'
from subprocess import Popen, PIPE
import time
import random

while True:
    rnd = random.randint(15,600)
    Popen(['mpg321', 'Assets/BridgeHorse.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)
    print "Sleeping for %i seconds." %rnd
    time.sleep(rnd)