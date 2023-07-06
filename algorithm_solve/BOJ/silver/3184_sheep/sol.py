import sys
sys.stdin = open('3184_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    v[x][y] = 1

    sheep = 0
    wolf = 0

    while q:
        cx, cy = q.popleft()
        if arr[cx][cy] == 'o':
            sheep += 1
        elif arr[cx][cy] == 'v':
            wolf += 1

        for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < R and 0 <= ny < C and v[nx][ny] == 0 and arr[nx][ny] != '#':
                q.append((nx,ny))
                v[nx][ny] = 1


    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0

    return wolf, sheep

R, C = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]

v = [[0] * C for _ in range(R)]


ww = 0
ss = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and v[i][j] == 0:
            w, s = bfs(i,j)
            ww += w
            ss += s
print(ss, ww)

