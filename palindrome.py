def palin(s):
    k=any([i for i in s if i<0])
    pal_arr=[] # if k=="True" its means negative number are present.
    if k==False:
        for i in s:
            temp=i
            rev=0
            while i!=0:
                rem=i%10
                rev=10*rev+rem
                if rev==temp:
                    pal_arr=pal_arr+[rev]
                i=i//10
    return any(pal_arr)
    
if __name__ == "__main__":
    len_=int(input())
    s=list(map(int,input().rstrip().split()))
    result=palin(s)
    print(result)
