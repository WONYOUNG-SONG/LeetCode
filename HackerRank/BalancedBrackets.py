#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    str_list = []
    matching_dict = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in matching_dict.values():
            str_list.append(char)
        elif char in matching_dict:
            if not str_list or str_list[-1] != matching_dict[char]:
                return "NO"
            str_list.pop()
    
    return "YES" if not str_list else "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
