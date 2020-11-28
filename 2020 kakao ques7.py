import numpy as np
from collections import deque
def sort_(state) : return sorted(state, key=lambda x : (x[0], x[1]))
def add(x, y) : return (x[0]+y[0], x[1]+y[1])
def check(head, tail) : return Board[head[0], head[1]] == 0 and Board[tail[0], tail[1]] == 0
def check_(state, move, cord) : return cord != state and cord not in move
def moving(head, tail) :
    state = sort_([head, tail])
    moving = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    move = [sort_([add(head,x), add(tail, x)]) for x in moving if check(add(head, x), add(tail, x))]
    rotating = [sort_([head, add(head, x)]) for x in moving  if check(head, add(head, x)) and check(tail, add(tail, x)) and check_(state, move, sort_([head, add(head, x)]))] +\
               [sort_([tail, add(tail, x)]) for x in moving  if check(head, add(head, x)) and check(tail, add(tail, x)) and check_(state, move, sort_([head, add(head, x)]))]
    return move+rotating
def solution(board):
    global Board, N
    N = len(board)
    Board = np.pad(board, ((1,1),(1,1)), 'constant', constant_values=1)
    que = deque([[(1, 1), (1, 2), 0]])
    visted = [[(1, 1), (1, 2)]]
    while que:
        head, tail, cost  = que.popleft()
        if head == (N, N) or tail == (N, N):
            return cost
        for child in moving(head, tail):
            if child not in visted:
                que.append([*child, cost+1])
                visted.append(child)
                
#board = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	

print(solution(board))
