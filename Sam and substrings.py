#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    ans = x = 0
    mod = 10**9 + 7
    for i, digit in enumerate(n, 1):

        x += int(digit) * i
        ans = (ans * 10 + x) % mod
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
