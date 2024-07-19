import sys
sys.stdin = open('2194_input.txt')

input = sys.stdin.readline

from collections import deque

def is_valid(x, y):
    if x < 0 or x + a > n or y < 0 or y + b > m:
        return False
    for i in range(a):
        for j in range(b):
            if arr[x+i][y+j] == 1:
                return False
    return True

def bfs():
    v = [[0] * m for _ in range(n)]
    q = deque([(sx-1, sy-1, 0)])
    v[sx-1][sy-1] = 1

    while q:
        cx, cy, dis = q.popleft()

        if cx == ex-1 and cy == ey-1:
            return dis

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy
            if is_valid(nx,ny) and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx, ny, dis+1))

    return -1

n, m, a, b, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

print(bfs())