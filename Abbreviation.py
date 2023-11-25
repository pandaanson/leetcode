#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    lena=len(a)
    lenb=len(b)
    dp=[[False for i in range(0,lenb+1)] for j in range(0,lena+1)]
    
    dp[0][0]=True
    for j in range(1,lena+1):
        if a[j-1].islower():
                    dp[j][0]=dp[j-1][0]
    for i in range(1,lenb+1):
        for j in range(1,lena+1):


            if a[j-1].isupper() and a[j-1]==b[i-1]:
                dp[j][i]=dp[j-1][i-1]
            elif a[j-1].islower() and a[j-1].upper()==b[i-1]:
                dp[j][i]=(dp[j-1][i-1] or dp[j-1][i])
            elif a[j-1].islower():
                dp[j][i]=(dp[j-1][i])

    if dp[-1][-1]:return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
