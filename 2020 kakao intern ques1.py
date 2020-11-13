#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:53:26 2020

@author: hms
"""
import numpy as np

def solution(numbers, hand):
    answer = ''

    keypad = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
              4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
              7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
              0 : [3, 1]}
    left = [3, 0]
    right = [3, 2]
    for i in numbers :
        if (i in [1, 4, 7])  :
            left = keypad[i]
            answer += 'L'
        elif (i in [3, 6, 9]) :
            right = keypad[i]
            answer += 'R'
        elif dist(left, keypad[i]) < dist(right, keypad[i]) :
            left = keypad[i]
            answer += 'L'
        elif dist(left, keypad[i]) > dist(right, keypad[i]) :
            right = keypad[i]
            answer += 'R'
        elif hand == 'left' :
            left = keypad[i]
            answer += 'L'
        else :
            right = keypad[i]
            answer += 'R'                
    return answer
def dist(a, b) :
    #return np.linalg.norm(np.array(a) - np.array(b))
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for i in range(10) :
    for j in range(10) :
        print("dist {} and {} is {}".format(i, j, dist(keypad[i], keypad[j])))

# 39min takes