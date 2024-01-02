import sys
sys.stdin = open('14716_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))

    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,-1),(-1,1),(1,1)):
            nx, ny = dx + cx, dy + cy

            if 0 <= nx < m and 0 <= ny < n and v[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx,ny))
                v[nx][ny] = 1

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

v = [[0] * n for _ in range(m)]

cnt = 0

for i in range(m):
    for j in range(n):
        if v[i][j] == 0 and arr[i][j] == 1:
            bfs(i,j)
            cnt += 1

print(cnt)