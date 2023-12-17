import sys
sys.stdin = open('2589_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))

    v = [[0] * m for _ in range(n)]
    v[x][y] = 1

    cnt = 0
    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == "L" and v[nx][ny] == 0:
                    v[nx][ny] = v[cx][cy] + 1
                    cnt = max(cnt, v[nx][ny])
                    q.append((nx,ny))
    return cnt-1


n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            ans = max(ans, bfs(i,j))
print(ans)