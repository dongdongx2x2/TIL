import sys
sys.stdin = open('2468_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = cx+dx, cy+dy

            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and arr[nx][ny] > a:
                v[nx][ny] = 1
                q.append((nx, ny))

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

max_h = max(map(max,arr))


ans = 0
for a in range(max_h+1):
    v = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > a and v[i][j] == 0:
                bfs(i,j)
                cnt += 1
    ans = max(cnt, ans)

print(ans)
