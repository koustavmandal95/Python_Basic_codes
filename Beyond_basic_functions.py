# extnded call for args arguments
def print_args(arg1,arg2,*args):
    print(arg1)
    print(arg2)
    print(args)
t=(12,23,45,66,77,88)
##extended call for kwargs
def color(red,green,blue,**kwargs):
    print("r:",red)
    print("g:",green)
    print("b:",blue)
    print(kwargs)
k={"red":23,"green":30,"blue":67,"alpha_red":455}

## Forwarding arguments
def trace(func,*args,**kwargs):
	print("args=",args)
	print("args=",kwargs)
	result=func(*args,**kwargs)
	print("ans=",result)
	return result
trace(int,'ff',base=32)
## zip technique
a=["kosuatva",1,3,4]
b=["anisha",123,33,45]
for i in zip(a,b):
    print(i)
## multiple array
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> c=[7,8,9]
>>> for i in zip(a,b,c):
	print(i)
common=[a,b,c]
for i in zip(common[0],common[1],common[2]):
	print(i)
# common becomes an args argument
from pprint import pprint as pp
pp(common)
for i in item(*common):
    print(i)
transposed=list(zip(*common))
