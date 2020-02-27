# https://www.hackerrank.com/challenges/crush
#!/bin/python3

import math
import os
import random
import re
import sys


class intersection:

    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
    def display(self):
        print('start: ', self.start)
        print('end: ', self.end)
        print('value: ', self.value)
# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    operations = []
    for i in range(len(queries)):
        op = intersection(queries[i][0], queries[i][1], queries[i][2])
        operations.append(op)
    for i in operations:
        i.display()


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print('result: ', result)
    #fptr.write(str(result) + '\n')

    # fptr.close()
