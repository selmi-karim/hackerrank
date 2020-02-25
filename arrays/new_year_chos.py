### https://www.hackerrank.com/challenges/new-year-chaos

#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    moves = 0
    valid = True
    for i in range(len(q),1,-1):
        if q[-1] == i:
            q.pop(-1)
        elif len(q) > 1 and q[-2] == i:
            q.pop(-2)
            moves += 1
        elif len(q) > 2 and q[-3] == i:
            q.pop(-3)
            moves += 2
        else:
            valid = False
            break
    if (not valid): print("Too chaotic")
    else: print(moves)       

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
