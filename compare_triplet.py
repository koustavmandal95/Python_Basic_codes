import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    Alice =0
    Bob=0
    for i in range(0,len(a)):
        if i==0:
            if a[0]>b[0]:
                Alice=Alice+1
                Bob=Bob
            elif a[0]<b[0]:
                Bob=Bob+1
                Alice=Alice
            elif a[0]==b[0]:
                Alice=Alice
                Bob=Bob
        if i==1:
            if a[1]>b[1]:
                Alice=Alice+1
                Bob=Bob
            elif a[1]<b[1]:
                Bob=Bob+1
                Alice=Alice
            elif a[1]==b[1]:
                Alice=Alice
                Bob=Bob
        if i==2:
            if a[2]>b[2]:
                Alice=Alice+1
                Bob=Bob
            elif a[2]<b[2]:
                Bob=Bob+1
                Alice=Alice
            elif a[2]==b[2]:
                Alice=Alice
                Bob=Bob
    return (Alice,Bob)
if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
   
