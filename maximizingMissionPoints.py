#!/bin/python

import math
import os
import random
import re
import sys


#mission input
nD_latD_long = raw_input().split()
n = int(nD_latD_long[0])
d_lat = int(nD_latD_long[1])
d_long = int(nD_latD_long[2])

mission_data = []

for n_itr in xrange(n):
    latitudeLongitude = raw_input().split()

    latitude = int(latitudeLongitude[0])

    longitude = int(latitudeLongitude[1])

    height = int(latitudeLongitude[2])

    points = int(latitudeLongitude[3])

    mission_data_list = []

    mission_data_list.append(latitude)
    mission_data_list.append(longitude)
    mission_data_list.append(height)
    mission_data_list.append(points)

    mission_data.append(mission_data_list)
print(mission_data)


       
