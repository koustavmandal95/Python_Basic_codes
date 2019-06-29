def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
if __name__== "__main__":

    x=int(input("enter the base number -->"))
    n=int(input("enter the power -->"))
    result=power(x,n)
    print(result)
