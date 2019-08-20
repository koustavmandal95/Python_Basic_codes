def patternA(N):
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(N+1):
        for j in range(0,i):
            print(a[i-1],end='')
        print('\r')
if __name__=="__main__":
    N=int(input())
    patternA(N)
N=10
o/p
A

BB

CCC

DDDD

EEEEE

FFFFFF

GGGGGGG

HHHHHHHH

IIIIIIIII

JJJJJJJJJJ
