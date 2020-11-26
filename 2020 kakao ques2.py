#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:42:53 2020

@author: hms
"""

p = "(()())()"	
#p = ")("	
#p = "()))((()"	
def solution(p):
    if p == '' : return ''
    u, v = split(p)
    return u + solution(v) if check_right(u) else '('+ solution(v) + ')' + reverse(u[1:-1]) 
def check_balance(p) :
    return True if sum(ord(x) for x in p) % 81 == 0 else False
def check_right(p) :
    count = 0
    for i in p :
        count += 1 if i == '(' else -1
        if count < 0 : return False
    return True
def split(p) :
    for i in range(1, len(p)+1) :
        if check_balance(p[:i]) :
            return p[:i], p[i:]
def reverse(p) :
    return ''.join(['(' if x==')' else ')' for x in p])


def solution(p):
    if p=='': return p
    right = True; balance=0
    for i in range(len(p)):
        balance += 1 if p[i] == ')' else -1
        if balance > 0: right = False
        if balance == 0:
            if right:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

list(map(lambda x:'(' if x==')' else ')',p[1:3]))
