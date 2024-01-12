# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

def solution(land):
    
    def bfs(x, y, idx):        
        q = deque()
        q.append((x,y))
        
        land[x][y] = idx
        cnt = 0
        
        while q:
            cx, cy = q.popleft()
            cnt += 1
            
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = cx + dx, cy + dy
                
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    q.append((nx,ny))
                    land[nx][ny] = idx
        return cnt
                    
    n = len(land)
    m = len(land[0])
    
    oil_records = {}
    oil_idx = 2
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                oil_records[oil_idx] = bfs(i,j,oil_idx)
                oil_idx += 1
    
    mx = 0
    for i in range(m):
        # 뭔가 들어갈것
        sm = 0
        sset = set()
        
        for j in range(n):
            
            if land[j][i] > 1 and land[j][i] not in sset:
                sset.add(land[j][i])
                sm += oil_records[land[j][i]]
        mx = max(mx, sm)                
            
    return mx