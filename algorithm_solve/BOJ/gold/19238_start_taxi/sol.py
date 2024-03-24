import sys
sys.stdin = open('19238_input.txt')

input = sys.stdin.readline

from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 이용한 최단 거리 탐색
def bfs(si, sj):
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return visited

# 승객을 찾고 목적지까지 이동
def find_and_move():
    global ci, cj, F
    for _ in range(m):
        # 현재 위치에서 각 승객까지의 거리를 찾음
        visited = bfs(ci, cj)
        # 가장 가까운 승객 찾기
        passenger = []
        for i in range(m):
            if not passengers[i]: continue
            si, sj, ei, ej = passengers[i]
            if visited[si][sj] != -1:
                passenger.append((visited[si][sj], si, sj, i))
        if not passenger:
            return False
        passenger.sort()
        dist, si, sj, idx = passenger[0]
        # 승객을 태운 후 목적지까지 이동
        F -= dist
        if F < 0:
            return False
        visited = bfs(si, sj)
        dist = visited[passengers[idx][2]][passengers[idx][3]]
        if dist == -1 or F - dist < 0:
            return False
        F += dist
        ci, cj = passengers[idx][2], passengers[idx][3]
        passengers[idx] = None
    return True

n, m, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ci, cj = map(int, input().split())
ci -= 1
cj -= 1
passengers = [None]*m
for i in range(m):
    si, sj, ei, ej = map(int, input().split())
    passengers[i] = (si-1, sj-1, ei-1, ej-1)

if find_and_move():
    print(F)
else:
    print(-1)