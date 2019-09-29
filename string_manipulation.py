>>> names=["Amy","John","George","Michael","Penelope"]
>>> biggest=max(len(name) for name in names)
>>> biggest
8
>>> for name in names:
	if len(name)==biggest:
		print(name)
Penelope
>>> k=[name for name in names if len(name)==8]
>>> k
['Penelope']
>>> for name in names:
	print(name.ljust(biggest,'-'))
Amy-----
John----
George--
Michael-
Penelope
>>> for name in names:
	print(name.rjust(biggest,'+'))
+++++Amy
++++John
++George
+Michael
Penelope
>>> for name in names:
	print(name.center(biggest,"="))
==Amy===
==John==
=George=
Michael=
Penelope
>>> base_string="koustav"
>>> trans_string=str.maketrans("av","27")
>>> trans_string
{97: 50, 118: 55} # unicode dictionary conversion 
>>> base_string.translate(trans_string)
'koust27'
>>> ord("a")
97
>>> ord("v")
118
>>> ord('2')
50
>>> ord('7')
55
>>> 
