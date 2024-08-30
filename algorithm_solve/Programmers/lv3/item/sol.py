# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2 , r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    arr[i][j] = 0
                elif arr[i][j] != 0:
                    arr[i][j] = 1
                    
    s = (characterX * 2, characterY * 2)
    e = (itemX * 2, itemY * 2)
    
    q = deque()
    q.append((s[0], s[1], 0))
    
    v = set()
    v.add((s[0], s[1]))
    
    while q:
        cx, cy, dis = q.popleft()
        
        if (cx,cy) == e:
            return dis // 2
        
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = cx + dx, cy + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and arr[nx][ny] == 1 and (nx, ny) not in v:
                q.append((nx, ny, dis + 1))
                v.add((nx,ny))
    
    return -1