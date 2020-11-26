import numpy as np

def solution(key, lock):
    N, M = len(lock), len(key)
    lock = np.pad(lock, ((M-1,M-1),(M-1,M-1)), 'constant', constant_values=0)
    for _ in range(4) :
        key = rotate(key)
        for i in range(M+N-1) :
            for j in range(M+N-1) :
                lock_ = np.array(lock)
                lock_[i:i+M, j:j+M] ^= key
                if lock_[M-1 : N + M-1, M-1 : N + M-1].sum() == N**2 :
                    return True
    return False

def rotate(key):
    return np.array(list(zip(*key[::-1])))