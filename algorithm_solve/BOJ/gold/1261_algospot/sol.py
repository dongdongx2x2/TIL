import sys
sys.stdin = open('1261_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1, 0), (-1, 0),(0, 1),(0, -1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 있는경우
                if arr[nx][ny] == 1 and dist[nx][ny] > dist[cx][cy] + 1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))

                elif arr[nx][ny] == 0 and dist[nx][ny] > dist[cx][cy]:
                    dist[nx][ny] = dist[cx][cy]
                    q.append((nx, ny))


m, n = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[1e9] * m for _ in range(n)]
dist[0][0] = 0

bfs(0, 0)
# print(dist)
print(dist[n-1][m-1])