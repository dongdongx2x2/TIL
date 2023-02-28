import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

arr = [list(input().rstrip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, visited):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, visited)
            cnt += 1

# 적녹색약
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            dfs(i, j, visited2)
            cnt2 += 1

print(cnt, cnt2)





