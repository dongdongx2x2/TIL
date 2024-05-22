import sys
sys.stdin = open('11967_input.txt')

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

switches = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switches[x - 1][y - 1].append((a - 1, b - 1))

# 불이 켜져 있는지 여부를 저장할 리스트
lights = [[False] * n for _ in range(n)]
lights[0][0] = True

# 방문 여부를 저장할 리스트
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

# 상하좌우 이동을 위한 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()

    # 현재 방에서 켤 수 있는 모든 방의 불을 켠다
    for (a, b) in switches[x][y]:
        if not lights[a][b]:
            lights[a][b] = True
            # 불을 켠 방이 인접한 방문된 방과 연결되어 있다면 큐에 추가
            for dx, dy in directions:
                nx, ny = a + dx, b + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                    queue.append((a, b))
                    visited[a][b] = True
                    break

    # 상하좌우 인접한 방 탐색ㄷ
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and lights[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))

result = sum(sum(row) for row in lights)
print(result)