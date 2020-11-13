#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:32:19 2020

@author: hms
"""
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#board = [[0,0,0],[0,0,0],[0,0,0]]
board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
def check(board, state) :
    h, w, direction, cost = state
    return 0 <= w < len(board) and 0 <= h < len(board) and board[h][w] != 1 and not(w == 0 and h == 0)
def make_state(h, w, direction) :
    if direction == 'up' : return [h-1, w, 'up', 100]
    elif direction == 'down' : return [h+1, w, 'down', 100]
    elif direction == 'right' : return [h, w+1, 'right', 100]
    else : return [h, w-1, 'left', 100]
def solution(board):
    init = [[0, 1, 'right', 100], [1, 0, 'down', 100]]
    DIRECTION = {'up':'down', 'down':'up', 'right':'left', 'left':'right'}
    que = [x for x in init if check(board, x)]
    for i in que : board[i[0]][i[1]] = 100
    
    while que :
        h, w, direction, cost = que.pop(0)
        directions = [inv_dir_ for dir_, inv_dir_ in DIRECTION.items() if direction != dir_]
        for i in directions :
            tmp = make_state(h, w, i)
            if not check(board, tmp) : continue
            tmp[3] += cost if i == direction else cost+500
            if board[tmp[0]][tmp[1]] == 0 or board[tmp[0]][tmp[1]] >= tmp[3] :
                board[tmp[0]][tmp[1]] = tmp[3]
                que.append(tmp)
    return board[-1][-1]



def print_board(board) :
    for i in board :
        print(i)
    print('-----------------')

print(solution(board))