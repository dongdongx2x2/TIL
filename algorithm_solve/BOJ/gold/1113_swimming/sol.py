import sys
sys.stdin = open('1113_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y, h):
    global ans

    q = deque()
    q.append((x,y))

    v[x][y] = 1

    flag = True
    cnt = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                flag = False
                continue

            if arr[nx][ny] <= h and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    if flag:
        ans += cnt

n, m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

ans = 0
for h in range(1, 9):
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] <= h and v[i][j] == 0:
                bfs(i,j,h)
print(ans)
