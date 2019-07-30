store=[]
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
        store.append(last_letter)
        print(store)
        print(last_letter)
    return sorted(strings,key=last_letter)
sort_by_last_letter(['hello','from',"ba",'india'])

g="global"
def outer(p="param"):
    l="local"
    def inner():
        print(g,p,l)
    inner()
outer()

def enclosing():
    def local_func():
        print("india")
    return local_func
lf=enclosing()
lf()

def enclose():
    x="Florida"
    def local_func():
        print(x)
    return local_func
lf=enclose()
lf()

def raise_to(exp):
    def raise_(x):
        return pow(x,exp)
    return raise_
square=raise_to(2)
square(5)

import time
def make_timer():
    last_called=None
    def elasped():
        nonlocal last_called
        now=time.time()
        if last_called is None:
            last_called=now
            return None
        result=now-last_called
        last_called=now
        return result
    return elasped
t=make_timer()
t()
t()
t()
t()
