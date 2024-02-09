# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    board = [list(x) for x in board]
    answer = 0
    
    tem = set()
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                char = board[i][j]
                if char == 0:
                    continue
                
                if board[i][j+1] == char and board[i+1][j] == char and board[i+1][j+1] == char:
                    tem.add((i,j))
                    tem.add((i,j+1))
                    tem.add((i+1,j))
                    tem.add((i+1,j+1))
        
        if tem:
            answer += len(tem)
            for i, j in tem:
                board[i][j] = 0     
            tem = set()
        else:
            break
            
        for i in range(m-1, -1, -1):
            for j in range(n):
                if board[i][j] == 0:
                    for k in range(i-1, -1, -1):
                        if board[k][j] != 0:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break
    
    return answer