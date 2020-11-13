#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:34:26 2020

@author: hms
"""
from itertools import combinations as cb

def solution(orders, course):
    for num_food in course :
        piv = []
        for foods in orders :
            if(len(foods) == num_food) :
                piv.append(foods)
        print(piv)
        print(orders)
        
    answer = [] 
    return answer


def pop_list(piv, lists) :
    ind = lists.index(piv)
    return lists[:piv] + lists[piv:]
    
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

solution(orders, course)

