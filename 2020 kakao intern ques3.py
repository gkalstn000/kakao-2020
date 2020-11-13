#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:35:59 2020

@author: hms
"""


#gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems = ["AA", "AB", "AC", "AA", "AC"]
#gems = ["XYZ", "XYZ", "XYZ"]
#gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
gems = [1,1,3,4,5,6,7,8,9]


def solution(gems):
    products = list(set(gems))
    l = 0
    r = 0
    bucket = {}
    answer = [0, len(gems)]
    while(l <= len(gems) and r <= len(gems)) :
        if len(bucket) == len(products) :
            if answer[1]-answer[0] > r-l:
                answer = [l, r]
            bucket[gems[l]] -= 1
            if bucket[gems[l]] == 0 : del bucket[gems[l]]
            l += 1
        else :
            try :
                if gems[r] in bucket : bucket[gems[r]] += 1
                else : bucket[gems[r]] = 1
            except :
                break
            r += 1
    answer[0] += 1
    return answer



print(solution(gems))
'''

    print('l : {}, r : {}'.format(l, r))
    print('gems :', gems)
    print('bucket :', bucket)
    print('answer :', answer)
    print("================")
'''