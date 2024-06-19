import sys
sys.stdin = open('22352_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(sx, sy):

    q = deque()
    q.append((sx, sy))
    v = [[0] * m for _ in range(n)]
    v[sx][sy] = 1
    tem_value = before[sx][sy]
    before[sx][sy] = after_value

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and after[nx][ny] == after_value:
                v[nx][ny] = 1
                q.append((nx,ny))
                after[nx][ny] = tem_value

n, m = map(int, input().split())

after = [list(map(int, input().split())) for _ in range(n)]
before = [list(map(int, input().split())) for _ in range(n)]

diff = []

for i in range(n):
    for j in range(m):
        if after[i][j] != before[i][j]:
            after_value = after[i][j]
            diff.append((i, j))

if not diff:
    print("YES")

else:
    sx, sy = diff[0]
    bfs(sx, sy)

    for i in range(n):
        for j in range(m):
            if after[i][j] != before[i][j]:
                print("NO")
                exit()
    print("YES")