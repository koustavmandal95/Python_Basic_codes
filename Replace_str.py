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

replace_str(s,a)
