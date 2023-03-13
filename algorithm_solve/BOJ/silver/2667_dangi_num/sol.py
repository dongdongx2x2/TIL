import sys
sys.stdin = open('2667_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(i,j,n):
    cnt = 1
    q = deque([])
    q.append((i,j))

    v[i][j] = 1

    while q:

        x, y = q.popleft()
        dx = [-1,1, 0, 0]
        dy = [0,0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = 1
                cnt += 1
    return cnt

N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:
            result.append(bfs(i ,j ,arr[i][j]))

print(len(result))

for i in sorted(result):
    print(i)



