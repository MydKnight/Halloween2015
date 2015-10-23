__author__ = 'madsens'
from subprocess import Popen, PIPE
import time

while True:
    Popen(['mpg321', 'Assets/BridgeHorse.mp3', '--loop', '0'], stdout=PIPE, close_fds=True)
    time.sleep(15)