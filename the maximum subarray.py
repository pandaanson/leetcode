#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    ans=[0,0]
    temparr=[]
    temp=0
    count=False
    for i in arr:
        if i>0:
            ans[1]+=i
            count=True
        if (temp<=0 and i<=0) or (temp>=0 and i>=0):
            temp+=i
        else:
            temparr.append(temp)
            temp=i
    temparr.append(temp)
    lentemp=len(temparr)
    dp=[[0,temparr[0]] for _ in range(lentemp)]
    for i in range(1,lentemp):
        dp[i][0]=max(dp[i-1])
        dp[i][1]=max(dp[i-1][1],0)+temparr[i]
    ans[0]=max(dp[-1])
        
    
    if not count:
        ans=[max(arr),max(arr)]
    return ans   
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
