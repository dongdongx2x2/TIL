import sys

sys.stdin = open('2206_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(x, y, break_cnt):
    q = deque()
    q.append((x, y, break_cnt))

    v = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    v[x][y][break_cnt] = 1

    while q:
        cx, cy, break_cnt = q.popleft()
        # print(v)
        if (cx, cy) == (N - 1, M - 1):
            return v[cx][cy][break_cnt]

        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M and v[nx][ny][break_cnt] == 0:
                if arr[nx][ny] == 0: # 벽 0 일떄
                    v[nx][ny][break_cnt] = v[cx][cy][break_cnt] + 1
                    q.append((nx, ny, break_cnt))

                else:
                    if break_cnt == 0:
                        v[nx][ny][break_cnt+1] = v[cx][cy][break_cnt] + 1
                        q.append((nx,ny,break_cnt+1))

    return -1


N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# v = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 0))
