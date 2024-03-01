# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True

def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]

def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    board = [[0] * (n+ 2*m) for _ in range(n + 2*m)]
    
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]
    
    rotate_key = key
    for _ in range(4):
        rotate_key = rotate90(rotate_key)

        for x in range(1, m+n):
            for y in range(1, m+n):
                attach(x,y,m, rotate_key, board)
                
                if check(board, m, n):
                    return True
                
                detach(x,y,m, rotate_key, board)
                
    return False