a=[2,4]
b=[16,32,96]
def inbtw(a,b):
    count=0
    factor=0
    count_=0
    count3=0
    factor2=0
    new_array=[]
    for i in b:
        for j in range(max(a),max(b)+1):
            if i%j==0:
                new_array=new_array+[j]
    set_array=set(new_array)
    new_array=list(set_array)
    print(new_array)
    filter1=[]
    filter2=[]
    for i in a:
        for j in new_array:
            if j%i==0:
                count=count+1
            if count == len(a):
                filter2=filter2+[j]
        count=0
    print(filter1)
    print(filter2)
    for i in new_array:
        for j in b:
            if j%i==0:
                count_=count_+1
            if count_==len(b):
                filter2=filter2+[i]
                factor2=factor2+1
        count_=0
    print("\r",factor2,filter2)
    filter3=[]
    for i in filter2:
        for j in a:
            if i%j==0:
                count3=count3+1
            if count3==len(a):
                filter3=filter3+[i]
        count3=0
    filter4=set(filter3)
    filter5=list(filter4)
    return len(filter5)
if __name__=="__main__":
    first_multiple_input = input("enter the array lengths with spaces-->").rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])
    arr=list(map(int,input("Enter the array -->").rstrip().split()))
    brr=list(map(int,input("Enter the second array -->").rstrip().split()))
    total=inbtw(arr,brr)
    print(total)
            
#inbtw(a,b)
