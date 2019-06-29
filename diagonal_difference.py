def diagonalDifference(arr):
    # Write your code here
    a=0
    b=0
    temp=len(arr)-1
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i==j:
                 a=a+arr[i][j]
    for i in range(0,len(arr)):
        for j in range(len(arr),-1,-1):
            b=b+arr[i][temp]
            print(b)
            temp=temp-1
            print(temp)
            break
    res=abs(a-b)
    print(a,b)
    return res
if __name__ == '__main__':
  

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("enter -->").rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
