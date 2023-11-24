#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    # Create a min-heap from the array A
    heapq.heapify(A)

    operations = 0
    while A and A[0] < k:
        # If there is only one cookie left and it's not sweet enough, return -1
        if len(A) == 1:
            return -1

        # Remove the two cookies with the least sweetness
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)

        # Combine the two cookies to create a new cookie
        new_sweetness = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, new_sweetness)

        operations += 1

    return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
