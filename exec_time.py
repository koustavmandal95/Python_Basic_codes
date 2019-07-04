import datetime
import time
def pattern(n):
    print("Counting the start time")
    start_time=datetime.datetime.now()
    for i in range(0,n):
        for j in range(0,i+1):
            print("#",end='')
        print("\r")
    time.sleep(60)
    end_time=datetime.datetime.now()
    result=end_time-start_time
    print("The exceution time is ->",result)


def pattern2(n):
    k=n
    print("Counting the start time")
    start_time=datetime.datetime.now()
    for i in range(0,n):
        for j in range(0,k):
            print(" ",end="")

        k=k-1
        for j in range(0,i+1):
            print("#",end="")
        print("\r")
    time.sleep(60)
    end_time=datetime.datetime.now()
    result=end_time-start_time
    print("The exceution time is ->",result)
    
pattern2(15)
