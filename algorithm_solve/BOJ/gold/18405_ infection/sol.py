import sys
sys.stdin = open('18405_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x,y):
    q = deque(virus)

    while q:
        v, cs, cx, cy = q.popleft()

        if cs == s:
            break

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
                arr[nx][ny] = v
                q.append((v, cs+1, nx, ny))

    return arr[x-1][y-1]

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j],0,i,j))

virus.sort()
print(bfs(x,y))



