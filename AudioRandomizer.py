__author__ = 'madsens'
from os import walk
import random
import os

def PlayRandomAudio(path, previousFile):
    #Play Random Audio File In Trixie folder.

    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    file = ""
    #Keep running getRandom until we get a new one
    while file == previousFile:
        file = getRandomFile(f)

    playFile = path + file
    os.system('mpg321 "%s" &' % playFile)
    #Returned played file to pass back on next scan.
    return file

def getRandomFile(f):
    return random.choice(f)