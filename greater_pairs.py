a=[89,24,00,8000,187,1888,1738]
def Greater_pairs(a):
    counter=0
    for i in range(0,len(a)):
        temp=i*a[i] # anyway
        if (i+1)<len(a):
            if i*a[i]<(i+1)*a[i+1]:
                temp=(i+1)*a[i+1]
                counter=counter+1
                print(((i+1),"-->",temp))
    print("the number of pairs are->",counter)

Greater_pairs(a)
