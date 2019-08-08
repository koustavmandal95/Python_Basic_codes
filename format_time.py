from datetime import datetime 
def main1():
    #%Y --> %Y, %H --> hour, %M -->Minutes %
    #%a/%A weekday [ex mon, thrus], %b/%B month[jan feb] ,%d day of month [0-31]                  
    now = datetime.now()
    print(now.strftime("Day:%a Month:%b Date:%d year:%y")) #o/p Day:Thu Month:Aug Date:08 year:19
    print(now.strftime("Day:%A Month:%B Date:%D year:%Y")) #o/p Day:Thursday Month:August Date:08/08/19 year:2019
    # %c --local's date %x time %X locale time
    print(now.strftime("Local date and time %c"))
    print(now.strftime("Local date and time %x"))
    print(now.strftime("Local date and time %X"))
    #%I/%H  -12/24 hour 
    print(now.strftime("Local date and time %I:%M:%S %p"))
    print(now.strftime("Local date and time %H:%M:%S"))
    # Complete Time
    print(now.strftime("Day-:%A Month-:%B Date-:%D year-:%Y Time: %I:%M:%S %p"))
    #o/pDay-:Thursday Month-:August Date-:08/08/19 year-:2019 Time: 01:02:18 PM

if __name__=="__main__":
    main1()