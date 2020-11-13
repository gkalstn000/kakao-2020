#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:27:25 2020

@author: hms

lang = cpp, java, python
work = backend, frontend
period= junior, senior
food = chicken, pizza
score
"""

def solution(info, query):
    answer = []
    return answer

def queryToList(query) :
    tmp = query.split()
    for i in range(3) :
        tmp.remove('and')
    print(tmp)
    return tmp
    
class Node :
    def __init__(self, lang, part, period, food, score) :
        self.lang = lang
        self.part = part
        self.period = period
        self.food = food
        self.score = score
        
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
a = "cpp and - and senior and pizza 250"
b=a.split()
b.remove('and')
b
queryToList(a)
