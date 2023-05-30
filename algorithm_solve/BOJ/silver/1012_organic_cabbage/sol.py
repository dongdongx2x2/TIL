import sys
sys.stdin = open('1012_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(x,y):

    q = deque()
    q.append((x,y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx,ny = cx+dx, cy+dy

            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == 1:
                v[nx][ny] = 1
                q.append((nx,ny))


T = int(input())

for _ in range(T):

    M, N, K = map(int,input().split())

    arr = [[0]*M for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        a, b = map(int,input().split())
        arr[b][a] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and v[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)


