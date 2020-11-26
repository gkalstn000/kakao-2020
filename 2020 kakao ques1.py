#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:25:23 2020

@author: hms
"""

s = "aabbaccc"
s = "ababcdcdababcdcd"
#s = "abcabcdede"
#s = "abcabcabcabcdededededede"	
#s = "xababcdcdababcdcd"


def solution(s):
    global index
    return min(press(s) for index in list(range(1, int(len(s)/2) + 1)) + [len(s)])

def press(s) :
    result = ''
    coef = 1
    while(len(s) > index) :
        piv = s[:index]
        s = s[index:]
        if piv != s[:index] :
            result += str(coef) + piv if coef != 1 else piv
            coef = 0
        coef += 1
    result += str(coef)+ s if coef != 1 else s
    return result
    
#=====================================================================================
text = s
tok_len = 3
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)



def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
compress(text, tok_len)





