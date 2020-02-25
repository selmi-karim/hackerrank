#### https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
 #!/bin/python3

import math
import os
import random
import re
import sys

def calcul(arr,i,j):
    return (sum(arr[i-1][j-1:j+2]) + arr[i][j] + sum(arr[i+1][j-1:j+2]))
# Complete the hourglassSum function below.
def hourglassSum(arr):
    res = -100
    for i in range(1,5):
        for j in range(1,5):
            #print(calcul(arr,i,j))
            res= max(res,calcul(arr,i,j))

    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

