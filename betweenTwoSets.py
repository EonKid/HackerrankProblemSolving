#!/bin/python

from __future__ import print_function

import os
import sys
# from fractions import gcd

#
# Complete the getTotalX function below.
#

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)    

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm,min_gcd+1,max_lcm) if min_gcd % x == 0])
    return count
    


nm = raw_input().split()
n = int(nm[0])

m = int(nm[1])

a = map(int, raw_input().rstrip().split())

b = map(int, raw_input().rstrip().split())

total = getTotalX(a, b)
print(total)

