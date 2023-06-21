import sys
sys.stdin = open('1600_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(x, y, K):
    q = deque()
    q.append((x, y, K))

    while q:
        cx, cy, cK = q.popleft()

        if cx == H-1 and cy == W-1:
            return v[cx][cy][cK]

        if cK:
            for dx, dy in horse:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < H and 0 <= ny < W and v[nx][ny][cK-1] == 0 and arr[nx][ny] == 0:
                    v[nx][ny][cK-1] = v[cx][cy][cK] + 1
                    q.append((nx,ny, cK-1))

        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and v[nx][ny][cK] == 0 and arr[nx][ny] == 0:
                v[nx][ny][cK] = v[cx][cy][cK] + 1
                q.append((nx, ny, cK))
    return -1


K = int(input())

W, H = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(H)]

v = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

delta = ((1,0),(-1,0),(0,1),(0,-1))
horse = ((-1, 2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1))

ans = bfs(0,0,K)
print(ans)


