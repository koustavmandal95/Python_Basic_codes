print("{:,}".format(1234456677))
#1,234,456,677
a,b=(input()).split()
print(type(a))
arr=[]
arr=list(map(int,input("Enter the list-> ").rstrip().split()))
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print(x,y,z)


from collections import OrderedDict
def main_dict():
    sportsTeams=[("Royals",(18,12)),("Rockets",(24,6)),("Cardinals",(20,10)),("Dragons",(22,8)),
                 ("Kings",(15,15)),("Chargers",(20,10)),("Jets",(16,14)),("Warriors",(25,5))]
    s=sorted(sportsTeams,key=lambda t:t[1][0],reverse=True)
    teams=OrderedDict(s)
    print(teams)
main_dict()
>>> a=[0]*4
>>> a
[0, 0, 0, 0]
>>> c=[]
>>> for _ in range(4):
	c.append(a)
>>> c
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
>>> for i,j in zip(range(3,-1,-1),range(3,-1,-1)):
	print(a[i][j])
>>> for i,j in zip(range(3,-1,-1),range(3,-1,-1)):
	print(c[i][j])

	
0
0
0
0
# The tricks with join
>>> a="abcxxdefxx"
>>> xa="".join(x for x in a if x!='x') # removing x from the string.
>>> xa
'abcdef'
>>>
