#!/bin/python3

import os
import sys
from datetime import time,datetime,date
import datetime
import time
#
# Complete the timeConversion function below.
#strptime

def timeConversion(s):
    c=s.split(":")
    hour=int(c[0])
    minute=int(c[1])
    if "AM" in c[2]:
        new_second=c[2].rstrip("AM")
        if hour==12:
            hour=0
    elif "PM" in c[2]:
        new_second=c[2].rstrip("PM")
        if hour==12:
            hour=12
        elif hour<12:
            hour=hour+12
    if minute<10:
        minute="0"+str(minute)
    if hour<10:
        hour="0"+str(hour)
    return ("%s:%s:%s"%(hour,minute,new_second))
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result+"\n")

    f.close()
