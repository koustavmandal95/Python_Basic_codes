from datetime import datetime
from datetime import date
from datetime import time

def _datetime_():
    tod=date.today()
    t=datetime.now()
    only_time=datetime.time(datetime.now()) #Important feature of python
    days=["monday","Tuesday","wednesday","Thrusday","Friday","saturday","sunday",]
    print("only the date:",tod)
    months=["Jan","Feb","mar","april","may","June","July","aug","Sept","Oct","Nov","Dec"]
    print("only the date:",tod.day,tod.month,tod.year)
    print("only the date:",t)
    print("only the date:",only_time)
    print(days[tod.weekday()])
    print(months[tod.month-1])
_datetime_()