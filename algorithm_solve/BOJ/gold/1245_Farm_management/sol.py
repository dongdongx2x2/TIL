import sys
sys.stdin = open('1245_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    v[x][y] = 1
    is_peak = True

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(-1, 1),(-1, -1),(1, -1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M:
                if arr[cx][cy] < arr[nx][ny]:
                    is_peak = False
                elif arr[cx][cy] == arr[nx][ny] and v[nx][ny] == 0:
                    q.append((nx, ny))
                    v[nx][ny] = 1
    return is_peak

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] and v[i][j] == 0:
            if bfs(i, j):
                cnt += 1
print(cnt)