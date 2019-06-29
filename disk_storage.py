import os
def disk_usage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total+=disk_usage(childpath)
    print("{0:<7}".format(total),path)
    return total

def sum_linear(s,n):
    if n==0:
        return 0
    else:
        return sum_linear(s,n-1)+s[n-1]


def reverse(s):
    if len(s)==1:
        return s
    else:
        return reverse(s[1:])+[s[0]]
if __name__ == "__main__":
    s=[]
    for _ in range(5):
        a=int(input("enter-->"))
        s.append(a)
    array=list(map(int, input("enter number with spaces->").rstrip().split()))
    #s.append(list(map(int, input("enter the number with spaces->").rstrip().split())))
    result1 = reverse(s)
    result2= reverse(array)
    print(result1,result2)
