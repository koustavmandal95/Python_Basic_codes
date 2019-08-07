def myfun(arg1,arg2,*k,suppressExceptions=False):
    print(arg1)
    print(arg2)
    print(k)
'''
def main():
    myfun(1,2,3,4,5,6,suppressExceptions=True)
'''
import collections
#namedtuple
def main1():
    Point=collections.namedtuple("Point","x y")
    p1=Point(10,20)
    p2=Point(30,40)
    print(p1,p2)
    print(p1.x,p2.y)
    p1=p1._replace(x=1000)
    print(p1)
#DefaultDict

def main():
    fruits=["apple","orange","banana","apple","Guava","banana","grape","apple"]
    fruitCounter={}
    for i in fruits:
        if i in fruitCounter.keys():
            fruitCounter[i]+=1
            print(fruitCounter)
        else:
            fruitCounter[i]=1
    for k,v in fruitCounter.items():
        print(k+":"+str(v))
        
from collections import defaultdict
fruits=['apple','pear','orange','banana','apple','grape','banana','banana']
fruitCounter=defaultdict(lambda:100)
for i in fruits:
    if i in fruitCounter.keys():
        fruitCounter[i]+=1
        print(fruitCounter)
#counter
from collections import Counter
fruits1=['apple','pear','orange','banana','apple','grape','banana','banana']
fruits2=["apple","orange","banana","apple","Guava","banana","grape","apple"]
c1=Counter(fruits1)
c2=Counter(fruits2)
print(c1["apple"])

c1.update(fruits2)
print(sum(c1.values()))
print(c1.most_common(3))
print(c1&c2)
#orderedDict
from collections import OrderedDict
def main_dict():
    sportsTeams=[("Royals",(18,12)),("Rockets",(24,6)),("Cardinals",(20,10)),("Dragons",(22,8)),
                 ("Kings",(15,15)),("Chargers",(20,10)),("Jets",(16,14)),("Warriors",(25,5))]
    s=sorted(sportsTeams,key=lambda t:t[1][0],reverse=True)
    teams=OrderedDict(s)
    print(teams)
    tw,wl=teams.popitem(False)
    print("top team:",tw,wl)
    for i,item in enumerate(teams,start=1):
        print(i,item)
        if i==4:
            break
main_dict()
