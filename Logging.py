__author__ = 'madsens'
import MySQLdb
import datetime

def LogAccess(rfid):
    # This file manages the connectivity to the database for logging access to the units. As a fallback, it
    # writes the access to a local log file
    db = MySQLdb.connect(host="mysql.shilohmadsen.com",
                  user="shilohmadsencom",
                  passwd="6DNN7Snp",
                  db="themagiccastle")

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime) VALUES (%s,1,%s);",(rfid,activationTime))
    print res
#if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.

def LogAudioAccess(rfid, filename):
    # This file manages the connectivity to the database for logging access to the units. As a fallback, it
    # writes the access to a local log file
    db = MySQLdb.connect(host="mysql.shilohmadsen.com",
                  user="shilohmadsencom",
                  passwd="6DNN7Snp",
                  db="themagiccastle")

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    #try to write access of the pi to a log file
    activationTime = datetime.datetime.now()
    activationTime = activationTime.strftime('%Y-%m-%d %H:%M:%S')
    res = cur.execute("INSERT INTO Activity (RFID, PIID, ActivationTime, FileName) VALUES (%s,1,%s, %s);",(rfid,activationTime, filename))
    print res
#if connect fails or if write fails, log connection failure to an error log and log the access to a local access log.