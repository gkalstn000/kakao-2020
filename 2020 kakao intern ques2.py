#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:35:01 2020

@author: hms
"""
import itertools 
import re
import copy

expression = "100-200*300-500+20"

def split_num(sepr_list, expression):
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, expression)
def split_sign(sepr_list, expression) :
    result = []
    for i in expression :
        if i in sepr_list : result.append(i)
    return result

def solution(expression):
    answer = []
    sepr_list = '*', '+', '-'
    nums = split_num(sepr_list, expression)
    signs = split_sign(sepr_list, expression)
    sign_kinds = set(signs)
    if(len(sign_kinds) == 1) : return abs(eval(expression))
    
    permu = list(itertools.permutations(sign_kinds, len(sign_kinds)))
    for i in permu : #conbinations 
        nums_ = copy.deepcopy(nums)
        signs_ = copy.deepcopy(signs)
        for j in i : #sign
            while(j in signs_) :
                ind = signs_.index(j)
                signs_.pop(ind)
                nums_[ind] = str(eval(nums_[ind] + j + nums_[ind+1]))
                nums_.pop(ind+1)
        
        answer.append(abs(eval(nums_[0])))
    return max(answer)


