#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    num_dict = dict()
    answer = []
    
    for num in arr:
        num_dict[num] = num_dict.get(num, 0) + 1
    
    for i in range(0, 100):
        if i not in num_dict:
            answer.append(0)
        else:
            answer.append(num_dict[i])
    return answer
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
