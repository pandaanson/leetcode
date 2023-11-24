#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

import heapq

def runningMedian(a):
    min_heap = []  # To store the larger half of the numbers
    max_heap = []  # To store the smaller half of the numbers
    medians = []

    for number in a:
        # Add the new number to one of the heaps
        if not max_heap or number < -max_heap[0]:
            heapq.heappush(max_heap, -number)  # We use negative values because Python has min-heap by default
        else:
            heapq.heappush(min_heap, number)

        # Rebalance the heaps if necessary
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate the median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2.0
        else:
            median = -max_heap[0] * 1.0

        medians.append(format(median, '.1f'))

    return medians
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
