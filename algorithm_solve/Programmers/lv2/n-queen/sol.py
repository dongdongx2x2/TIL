# https://school.programmers.co.kr/learn/courses/30/lessons/12952
def solution(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
        for i in range(row):
            if abs(board[i] - col) == abs(i-row):
                return False
        return True
    
    
    def dfs(board, row):
        if row == n:
            return 1
        cnt = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                cnt += dfs(board, row + 1)
        return cnt
    
    board = [-1] * n    
    return dfs(board, 0)