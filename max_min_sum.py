def maxmin(arr):
    arr.sort(reverse=False)
    print(arr)
    len_=len(arr)
    minsum=0
    maxsum=0
    for i in range(0,len_-1):
        minsum=minsum+arr[i]
    print(minsum)
    for j in range(1,len_):
        maxsum=maxsum+arr[j]
    print(maxsum)
   
if __name__=="__main__":
    arr=list(map(int,input("Enter the array with spaces ---->").rstrip().split()))
    result=maxmin(arr)
    
