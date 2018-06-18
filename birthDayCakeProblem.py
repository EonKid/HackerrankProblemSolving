#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    max_num = ar[0]
    for num in ar:
        if max_num <= num:
            max_num = num
    max_count = 0
    for num in ar:
        if max_num == num:
            max_count += 1
    return max_count
    

ar_count = int(raw_input())
ar = map(int, raw_input().rstrip().split())
result = birthdayCakeCandles(ar)
print(result)
    