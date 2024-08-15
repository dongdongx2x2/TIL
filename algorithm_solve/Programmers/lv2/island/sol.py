# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque

def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append((x,y))
        v[x][y] = 1
        sm = int(maps[x][y])
        
        while q:
            cx, cy = q.popleft()
            
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = cx + dx, cy + dy
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and v[nx][ny] == 0 and maps[nx][ny] !="X":
                    q.append((nx,ny))
                    sm += int(maps[nx][ny])
                    v[nx][ny] = 1
        return sm
    
    answer = []
    v = [[0] * len(maps[0]) for _ in range(len(maps))]
         
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and v[i][j] == 0:
                answer.append(bfs(i,j))
                
    answer.sort()
    if not answer:
        return [-1]
    
    return answer