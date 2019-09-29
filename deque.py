>>> import collections
>>> d=collections.deque('abcdefg')
>>> d
deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
>>> d.appendleft(1)
>>> a
[2, 3, 5]
>>> d
deque([1, 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
>>> d.append(2)
>>> d
deque([1, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 2])
>>> d.pop()
2
>>> d
deque([1, 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
>>> 
>>> d.popleft()
1
>>> d
deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
>>> d.rotate()
>>> d
deque(['g', 'a', 'b', 'c', 'd', 'e', 'f'])
>>> d.rotate()
>>> d
deque(['f', 'g', 'a', 'b', 'c', 'd', 'e'])
>>> d.rotate()
>>> d
deque(['e', 'f', 'g', 'a', 'b', 'c', 'd'])
>>> d.maxlen()
>>> d.count('e')
1
>>> for elem in d:
	print(elem,end=',')

	
e,f,g,a,b,c,d,
>>> for elem in d:
	print(elem.upper(),end=',')

	
E,F,G,A,B,C,D,
>>> for elem in range(len(d)):
	print(d[elem],end=',')

	
e,f,g,a,b,c,d,
>>> for elem in range(len(d)):
	print(d[elem].upper(),end=',')

	
E,F,G,A,B,C,D,
>>> len(d)
7
