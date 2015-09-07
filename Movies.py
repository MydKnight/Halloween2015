__author__ = 'shilohmadsen'
#This file sends the UDP commands to localhost to trigger the play movie
import socket
import subprocess
import os

def PlayMovie ():
    #print ("playing movie")

    UDP_IP = "localhost"
    UDP_PORT = 4444
    MESSAGE = "looper/set:intermission"

    sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    os.system('stty sane')
    return

def StartLoop():
    subprocess.Popen(['sudo', '/home/pi/info-beamer-pi/info-beamer', '/home/pi/loopscript'])
    #print "Starting Movie Loop"
    return

def StopLoop():
    subprocess.Popen(['sudo','pkill', 'info-beamer'])
    #print "Starting Movie Loop"
    return