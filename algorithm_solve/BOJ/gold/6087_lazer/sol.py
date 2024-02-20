import sys
sys.stdin = open('6087_input.txt')

input = sys.stdin.readline

from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(sx, sy):
    q = deque()

    for i in range(4):
        q.append((sx,sy,i,0))
        v[sx][sy][i] = 0

    while q:
        x, y, dir, mir = q.popleft()
        nx, ny = x + dx[dir], y + dy[dir]

        while True:
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if arr[nx][ny] == "*":
                break

            if v[nx][ny][dir] < mir:
                break

            if v[nx][ny][dir] > mir:
                v[nx][ny][dir] = mir
                for i in range(4):
                    if i != dir:
                        q.append((nx,ny,i,mir+1))
            nx = nx + dx[dir]
            ny = ny + dy[dir]

m, n = map(int, input().split())

C = []
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))
    for j in range(m):
        if arr[i][j] == 'C':
            C.append((i,j))
INF = float("inf")
v = [[[float("inf")] * 4 for _ in range(m)] for _ in range(n)]
# print(C)
bfs(C[0][0],C[0][1])
print(min(v[C[1][0]][C[1][1]]))
