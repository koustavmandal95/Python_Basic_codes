if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=False)
    len_=len(arr)
    highest=arr[len_-1]
    second_high=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<highest:
            second_high=arr[i]
            print(second_high)
            break
