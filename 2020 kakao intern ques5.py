#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:53:04 2020

@author: hms
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
case1 = [9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]]
case2 = [9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]]
case3 = [9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]]
n, path, order  = case3

def get_key(diction, val) :
    for k, v in diction.items() :
        if v == val : return k
def solution(n, path, order):
    graph = {n: [] for n in range(n)}
    for a, b in path :
        graph[a].append(b)
        graph[b].append(a)
    order_ = defaultdict()
    for p, a in order :
        if a == 0 : return False
        order_[a] = p
    visited = list()
    stack = [0]
    wait = [0 for _ in range(n)]
    while stack  :
        node = stack.pop()
        if node in visited : continue
        if node in order_.keys():
            wait[node] = 1
            continue
        after = get_key(order_, node)
        if after :
            if wait[after] :
                wait[after] = 0
                visited.append(after)
                stack.extend(graph[after])
            
            del order_[after]
        #default
        visited.append(node)
        stack.extend(graph[node])
    return True if sum(wait) == 0 else False

print(solution(n, path, order))

 

'''
def solution(n, path, order):
    before = [0 for _ in range(n)]
    after = [0 for _ in range(n)]
    visit = [0 for _ in range(n)]
    graph = {n: [] for n in range(n)}
    
    for a, b in path :
        graph[a].append(b)
        graph[b].append(a)
        
    for p, a in order :
        if a == 0 : return False
        before[a] = p
    
    visit[0] = 1
    stack = graph[0]
    while stack  :
        node = stack.pop()
        if visit[node] : continue
        if not visit[before[node]] :
            after[before[node]] = node
            continue
        visit[node] = 1
        stack.extend(graph[node])
        stack.append(after[node])
    return True if sum(visit) == n else False

'''