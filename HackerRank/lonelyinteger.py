#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    '''
    num_dict = dict()
    
    for num in a:
        num_dict[num] = num_dict.get(num, 0) + 1
    
    for key, val in num_dict.items():
        if val == 1:
            return key
    '''
    answer = []
    
    for num in a:
        if num in answer:
            answer.remove(num)
        else:
            answer.append(num)
    
    return answer[0]
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
