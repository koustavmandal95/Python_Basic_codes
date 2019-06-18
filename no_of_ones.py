a=[12,24,22,17,187,18889076,2223,173]
def no_of_ones(a):
    j=0
    for i in a:
        temp=i
        while temp>10:
            temp=temp//10
            if temp==1:
                j=j+1
    print("The number of ones are --->",j)
no_of_ones(a)
