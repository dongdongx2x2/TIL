import sys
sys.stdin = open('2146_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    v[x][y] = num

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = num

def bridge(number):
    q = deque()
    dis = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if v[i][j] == number:
                dis[i][j] = 0
                q.append((i,j))

    while q:
        cx, cy = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy

            if 0<=nx<n and 0<=ny<n:
                if v[nx][ny] and v[nx][ny] != number:
                    return dis[cx][cy]

                elif v[nx][ny] == 0 and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[cx][cy] + 1
                    q.append((nx, ny))
    return 1e9


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] and v[i][j] == 0:
            bfs(i,j)
            num += 1

mimi = 1e9
for i in range(1, num):
    mimi = min(mimi, bridge(i))

print(mimi)
