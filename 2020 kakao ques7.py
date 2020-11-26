#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:59:02 2020

@author: hms
"""
def move(state) :
    h, w, direction, cost = state
        
    
    
    
    
    
    
    if Board[h][w] == 1 or (w == 0 and h == 0) : return False
    if direction == 'u' :
        return 0 <= w < len(Board) and 0 <= h < len(Board)-1 and Board[h-1][w] != 1
    elif direction == 'd' :
        return 0 <= w < len(Board) and 1 <= h < len(Board) and Board[h+1][w] != 1 
    elif direction == 'r' :
        return 0 <= w < len(Board)-1 and 0 <= h < len(Board) and Board[h][w+1] != 1
    else :
        return 1 <= w < len(Board) and 0 <= h < len(Board) and Board[h][w-1] != 1 

    
    
    
def solution(board):
    global Board
    Board = board
    
    init = [[0, 0, 'r', 0]]
    
    
    
    return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	
solution(board)

'''
    DIRECTION = {'up':'down', 'down':'up', 'right':'left', 'left':'right'}
    ORDER = {'HC' : 'HCC', 'HCC' : 'HC', 'TC' : 'TCC', 'TCC' : 'TC'}
'''
ord('r')
ord('l')
ord('u')
ord('d')
