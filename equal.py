#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    min_chocolates = min(arr)
    ans = float('inf')

    for base in range(5):
        current_operations = 0
        for chocolates in arr:
            delta = chocolates - min_chocolates + base
            current_operations += delta // 5 + delta % 5 // 2 + delta % 5 % 2
        ans = min(ans, current_operations)

    return ans
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
