__author__ = 'madsens'
import datetime
import time
import Logging

lastScan = 0


while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "stop":
        print "Stop Encountered. Exiting"
        break  # stops the loop
    else :
        #Insert various function calls to run files etc.
        #Check time of day. If within certain hours, do X, else do Y. In both cases, restrict by timer as well
        now = datetime.datetime.now()
        print "Hour: ",now.hour
        print "Current Scan: ", currentScan
        if currentScan - lastScan < 15:
            print "Too Soon. Wait 15 seconds"
            print "Elapsed Time: ", currentScan - lastScan
        else:
            print "Trigger gag and reset the last run variable"
            Logging.LogAccess(n)
            lastScan = currentScan

