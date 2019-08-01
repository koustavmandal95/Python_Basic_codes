def compress(s):
    number="0123456789"
    count=1
    f_cnt=1
    pos=0
    tup="({},{})".format(0,0)
    a=[int(i) for i in s]
    for i in range(0,len(a)):
        if pos==len(a)-1:
            if a[i]==a[pos-1]:
                count=f_cnt+1
                tup="({},{})".format(count-1,a[i])
            else:
                count=1
                tup="({},{})".format(count,a[i])
            print(tup,end='')
        elif a[i]==a[i+1]:
            count=count+1
            f_cnt=count
        else:
            tup="({},{})".format(count,a[i])
            print(tup,end='')
            count=1
        pos=pos+1
        
        
if __name__=="__main__":
    s=input("Enter the string")
    compress(s)
        
#(1, 1) (3, 2) (1, 3) (2, 1)
