#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:41:02 2020

@author: hms
"""

from itertools import permutations
def solution(n, weak, dist):
    answer = []
    dists = [list(x) for x in permutations(dist)]
    weaks = [weak] + [weak[i+1:]+[x+n for x in weak[:i+1]] for i, _ in enumerate(weak[:-1])]
    print(weaks)
    for weak in weaks :
        for dist in dists :
            check = weak[0]
            for i, d in enumerate(dist) :
                check += d
                if check >= weak[-1] :
                    answer.append(i)
                    break
                else :
                    check = [x for x in weak if x > check][0]
    return min(answer)+1 if answer else -1
