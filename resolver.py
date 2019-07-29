import socket
class Resolver:
	def __init__(self):
		self._cache={}
	def __call__(self,host):
		if host not in self._cache:
			self._cache[host]=socket.gethostbyname(host)
		return self._cache[host]
	def clear(self):
		self._cache.clear()
	def has_host(self,host):
		return host in self._cache

a=Resolver()
a("google.com")

def seq_immutable(immutable):
	if immutable==True:
		cls=tuple
	else:
		cls=list
	return cls
#seq=seq_immutable(immutable=False)
#from Resolver import seq_immutable
def sequence_class(immutable):
	return list if immutable else tuple

a=['Gautam Gambhir', 'Ms Dhoni', 'Rahul Dravid', 'Suresh Raina', 'Virat Kohli', 'Yuvraj Singh']
sorted(a,key=lambda name:name.split()[-1])

def hypervolume(*lengths):
    i=iter(lengths)
    v=next(i)
    for length in i:
        v=v*length
    print(v)
hypervolume(21,3)

# Revised version
def _hypervolume(length,*lengths):
	v=length
	for item in lengths:
		print(item)
_hypervolume(3,5,7,9)
