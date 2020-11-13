#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:11:54 2020

@author: hms
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""

def solution(new_id):
    strings = "abcdefghijklmnopqrstuvwxyz0123456789-_. "
    answer = ''
    if rule(new_id) : return new_id
    #step 1
    new_id = new_id.lower()
    print(new_id)
    if rule(new_id) : return new_id
    #step 2
    for char in new_id :
        if char in strings :
            answer += char
    new_id = answer
    print(new_id)
    if rule(new_id) : return new_id
    answer = ''
    #step 3
    new_id = delpoint(new_id)
    print(new_id)
    if rule(new_id) : return new_id
    #step 4
    if new_id[0] == '.' :
        new_id = new_id[1:]
    try :
        if new_id[-1] == '.' : 
            new_id = new_id[:-1]
    except :
        print("")
    print(new_id)
    if rule(new_id) : return new_id
    #step 5
    new_id = new_id.replace(" ", "a")
    print(new_id)
    if rule(new_id) : return new_id
    #step 6
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.' :
            new_id = new_id[:14]
    print(new_id)  
    if rule(new_id) : return new_id
    #step 7
    try :
        if len(new_id) <= 2 :
            while len(new_id) != 3 :
                new_id += new_id[-1]
    except :
        return "aaa"
    return new_id


def delpoint(new_id) :
    answer = ''
    tmp = ''
    for char in new_id :
        if char == '.' :
            tmp += char
        else : 
            answer += ''.join(set(tmp)) + char
            tmp = ''
    return answer + ''.join(set(tmp))
        
        
def rule(new_id) :
    strings = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    if(len(new_id) <3 or len(new_id) > 15) :
        return False
    for char in new_id :
        if(not char in strings) :
            return False
    if new_id[0] == '.' or new_id[len(new_id)-1] == '.' :
        return False
    if new_id.find(".") != -1 :
        index = new_id.find(".")
        if new_id[index+1] == "." :
            return False
    return True

id = "abcdefghijklmn.p"
print(solution(id))
