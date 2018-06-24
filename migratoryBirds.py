#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/migratory-birds/problem
def migratoryBirds(arr):
    arr_types = [0]*5
    for type in arr:
        count = arr_types[type-1]
        count += 1
        arr_types[type-1] = count
    return arr_types.index(max(arr_types)) + 1   
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()