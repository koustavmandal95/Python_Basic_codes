from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

def timedelta_():
    now=datetime.now()
    print(str(now))
    print(timedelta(days=365,hours=8,minutes=10))
    print("Time from now:"+str(now+timedelta(days=365)))
    print("Time from now:"+str(now+timedelta(days=2,weeks=4)))
    net_time=datetime.now()-timedelta(days=7,hours=4,minutes=23)
    print(net_time.strftime("%A %B %D %H:%M:%S %p")) #o/p Thursday August 08/01/19 10:20:49 AM
def find_april_fool():
    today=date.today()
    afd=date(today.year,4,1)
    if afd < today:
        print("The april fool went %d days ago"%((today-afd).days))
    afd=afd.replace(year=today.year+1)
    apr_to_be=afd-today
    print("The next april fool will come in:",apr_to_be.days)
if __name__=="__main__":
    timedelta_()
    find_april_fool()
