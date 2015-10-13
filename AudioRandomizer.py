__author__ = 'madsens'
from os import walk
import random
import os

def PlayRandomAudio(path):
    #Play Random Audio File In Trixie folder.
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    file = random.choice(f)
    playFile = path + file
    os.system('mpg321 "%s" &' % playFile)