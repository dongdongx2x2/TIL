import sys
sys.stdin = open('4963_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and v[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx,ny))
                v[nx][ny] = 1



while True:
    w, h = map(int,input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int,input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i,j)
                cnt += 1

    print(cnt)