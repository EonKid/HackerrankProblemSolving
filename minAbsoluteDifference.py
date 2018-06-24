import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_difference = 10**20
    for i in range(0,len(arr)-1):
        absolute_difference = abs(arr[i] - arr[i+1])
        if min_difference > absolute_difference:
            min_difference = absolute_difference
    return min_difference            

n = int(raw_input())

arr = map(int, raw_input().rstrip().split())

result = minimumAbsoluteDifference(arr)
print(result)