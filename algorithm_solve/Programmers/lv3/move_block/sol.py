# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos1, pos2 = pos
    pos1_x, pos1_y = pos1
    pos2_x, pos2_y = pos2
    
    # 4가지 이동 가능(상, 하, 좌, 우)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        next_pos1 = (pos1_x + move[0], pos1_y + move[1])
        next_pos2 = (pos2_x + move[0], pos2_y + move[1])
        if board[next_pos1[0]][next_pos1[1]] == 0 and board[next_pos2[0]][next_pos2[1]] == 0:
            next_pos.append((next_pos1, next_pos2))
    
    # 회전 가능 여부 확인
    if pos1_x == pos2_x: # 로봇이 가로로 놓여 있는 경우
        for i in [-1, 1]: # 위로 회전, 아래로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append(((pos1_x + i, pos1_y), pos1))
                next_pos.append(((pos2_x + i, pos2_y), pos2))
    elif pos1_y == pos2_y: # 로봇이 세로로 놓여 있는 경우
        for i in [-1, 1]: # 왼쪽으로 회전, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append((pos1, (pos1_x, pos1_y + i)))
                next_pos.append((pos2, (pos2_x, pos2_y + i)))
    
    return next_pos

def solution(board):
    n = len(board)
    # 맵 외곽에 벽 추가 (경계 처리를 위함)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    # BFS 수행
    q = deque([(((1, 1), (1, 2)), 0)]) # 위치, 시간
    visited = set([((1, 1), (1, 2))]) # 방문 처리
    
    while q:
        pos, time = q.popleft()
        # (n, n) 위치에 도달하면 종료
        if (n, n) in pos:
            return time
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, time + 1))
                visited.add(next_pos)

    return 0