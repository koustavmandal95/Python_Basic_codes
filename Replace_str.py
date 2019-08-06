              ||
#siva code ///  \\\\
def replace_str(s,a):
    s=list(s)
    a=list(a)
    for i in range(0,len(s)):
        if s[i-1]==" " or i==0:
            if s[i:i+len(a)]==a:
                s[i:i+len(a)]='*'*len(a)
    k="".join(s)
    print(k)
s=input()
a=input()                                   ||
def reverse_replace_str(s,a): #siva code ///  \\\\
    s=list(s)
    temp=a
    a=list(a)
    temp=list(temp)
    k=[temp[i] for i in range(len(temp)-1,-1,-1)]
    k="".join(k)
    for i in range(0,len(s)):
        if s[i-1]==" " or i==0:
            if s[i:i+len(a)]==a:
                s[i:i+len(a)]=k
    k="".join(s)
    print(k)

reverse_replace_str(s,a)


replace_str(s,a)
