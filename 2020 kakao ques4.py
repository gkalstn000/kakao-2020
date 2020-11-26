#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:49:09 2020

@author: hms
"""

import re

def solution(words, queries):
    answer = []
    trees = [Trie() for _ in range(10000)]
    inv_trees = [Trie() for _ in range(10000)]
    for word in words :
        trees[len(word)-1].insert(word)
        inv_trees[len(word)-1].insert(word[::-1])
    for query in queries :
        if query[0] == '?' :
            answer.append(inv_trees[len(query)-1].query(re.sub('[^a-z]', '', query[::-1])))
        else :
            answer.append(trees[len(query)-1].query(re.sub('[^a-z]', '', query)))
    return answer

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.counter = 0
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            node.counter += 1
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.counter += 1
    def query(self, word) :
        node = self.root
        for char in word :
            if char not in node.children : return 0
            node = node.children[char]
        return node.counter
            
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
tree = Trie()
tree.insert('abs')
tree.root.counter
root = tree.root
child = root.children['s']
child.children
