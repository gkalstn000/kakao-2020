#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:09:29 2020

@author: hms
"""


def solution(n, build_frame):
    global N
    N = n
    answer = []
    for frame in build_frame :
        if frame[3] == 1 :
            answer.append(frame[:-1])
            if not check_rule(answer) : answer.pop()
        else :
            del answer[answer.index(frame[:-1])]
            if not check_rule(answer) : answer.append(frame[:-1])
    answer.sort()
    return answer
def check_rule(answer) :
    for frame in answer :
        x, y, structure = frame
        if x < 0 or y < 0 or x > N or y > N : return False
        if structure == 0 :
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer : continue
            else : return False
        else :
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) : continue
            else : return False
    return True


build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5
a = solution(n, build_frame)
a
a.sort()
a
