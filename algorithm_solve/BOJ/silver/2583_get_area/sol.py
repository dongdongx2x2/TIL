import sys
sys.stdin = open('2583_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(x,y):

    q = deque()
    q.append((x,y))
    v[x][y] = 1

    cnt = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < M and 0 <= ny < N and v[nx][ny] == 0 and arr[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1
                cnt += 1
    return cnt



M, N, K = map(int, input().split())

arr = [[0]* N for _ in range(M)]
# pprint(arr)
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1


v = [[0] *N for _ in range(M)]

ans = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and v[i][j] == 0:
            ans.append(bfs(i,j))
print(len(ans))
print(*sorted(ans))