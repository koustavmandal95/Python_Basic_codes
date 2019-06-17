import threading

import time
import datetime
#i=100
def loop1_10():
    print(datetime.datetime.now())
    for i in range(10,1,-1):
        time.sleep(1)
        print(" Wait for 1 seconds--->",i)
        print(datetime.datetime.now())
threading.Thread(target=loop1_10).start()
'''
import threading 
  
def gfg(): 
    print("GeeksforGeeks\n") 
  
timer = threading.Timer(500.0, gfg)
print("Entering the Timer")
timer.start() 
print("Cancelling timer\n") 
timer.cancel() 
print("Exit\n") 
'''
