#String Format
# 1. Repr has the power to overwrite str
class Person():
    def __init__(self):
        self.fname="Joe"
        self.lname="Marini"
        self.age=25
    def __repr__(self):
        return "<person class -fname:{0},lname:{1},age: {2}>".format(self.fname,self.lname,self.age)
    def __str__(self):
        return "name:{0},title:{1}, age:{2}".format(self.fname,self.lname,self.age)
    def __bytes__(self):
        val="Person:{0}:{1}:{2}".format(self.fname,self.lname,self.age)
        return bytes(val.encode('utf-8'))
def main():
    cls1=Person()
    print(repr(cls1))
    print(str(cls1))
    print("Formattted:{0}".format(cls1)) # this is equivalent to str function.
    print(bytes(cls1))

#Computed attributes
class mycolor():
    def __init__(self):
        self.red=50
        self.green=75
        self.blue=100
    def __getattr__(self,attr):
        if attr=="rgbcolor":
            return (self.red,self.green,self.blue)
        elif attr=="hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red,self.green,self.blue)
        else:
            raise AttributeError
    def __setattr__(self,attr,val):
        if attr=="rgbcolor":
            self.red=val[0]
            self.green=val[1]
            self.blue=val[2]
        else:
            super().__setattr__(attr,val)
    def __dir__(self):
        return ("red","green","blue","rgbcolor","hexcolor")
def main2():
    cls1=mycolor()
    print((cls1.rgbcolor))
    print((cls1.hexcolor))
    cls1.rgbcolor=(125,200,15)
    print((cls1.rgbcolor))
    print((cls1.hexcolor))
    print(dir(cls1))
    
#Class Numerical Operators
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "<Point({0},{1})>".format(self.x,self.y)
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __add__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __iadd__(self,other):
        self.x+=other.x
        self.y+=other.y
        return self
def main3():
        p1=Point(10,20)
        p2=Point(30,40)
        p3=Point(50,70)
        p4=Point(60,80)
        print(p1,p2)
        p5=p1+p2
        p3+=p4
        print(p3)
    
#object comparisions
class Employee():
    def __init__(self,fname,lname,level,yrsService):
        self.fname=fname
        self.lname=lname
        self.level=level
        self.seniority=yrsService
    def __ge__(self,other):
        if self.level==other.level:
            return self.seniority>=other.seniority
        return self.level>=other.level
    def __gt__(self,other):
         return self.level>other.level
    def __lt__(self,other):
        pass
    def __le__(self,other):
        pass
    def __eq__(self,other):
        pass
def main4():
    dept=[]
    dept.append(Employee("Tim","Sims",5,9))
    dept.append(Employee("John","Dons",4,12))
    dept.append(Employee("Jane","Smith",6,6))
    dept.append(Employee("Rebecca","Robinson",5,13))
    dept.append(Employee("Tyler","Durden",5,12))
    print(dept[0]>=dept[2])
    print(dept[4]>dept[3])
    
