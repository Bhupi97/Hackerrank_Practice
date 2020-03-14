#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l = len(arr)
    a1 = []
    maxi = 0
    mini = 0
    a1 = sorted(arr)

    for i in range(l-1):
        mini += a1[i]
    
    for j in range(l-1,0,-1):
        maxi += a1[j]

    

    print(mini,maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
