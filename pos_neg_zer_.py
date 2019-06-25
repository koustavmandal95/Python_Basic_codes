import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    length=len(arr)
    for i in arr:
        if i<0:
            neg=neg+1
        elif i>0:
            pos=pos+1
        elif i==0:
            zer=zer+1
    _pos=pos/length
    _neg=neg/length
    _zer=zer/length
    print("{0:.5f}".format(_pos))
    print("{0:.5f}".format(_neg))
    print("{0:.5f}".format(_zer))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
