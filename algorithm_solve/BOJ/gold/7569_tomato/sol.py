import sys
sys.stdin = open('7659_input.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    global zero_cnt
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    q = deque()

    for a, b, c in bfstem:
        q.append((a,b,c))

        v[a][b][c] = 1

    while q:
        cz,cx,cy = q.popleft()

        for dz, dx, dy in ((0,1,0), (0,-1,0), (0,0,1), (0,0,-1), (1,0,0), (-1,0,0)):
            nz, nx, ny = cz + dz, cx + dx, cy + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and v[nz][nx][ny] == 0 and arr[nz][nx][ny] == 0:
                v[nz][nx][ny] = v[cz][cx][cy] + 1
                q.append((nz,nx,ny))
                zero_cnt -= 1

    if zero_cnt == 0:
        return v[cz][cx][cy]-1
    else:
        return -1


M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# v = [[[0] * M for _ in range(N)] for _ in range(H)]
# print(v)

zero_cnt = 0
bfstem = []
for i in range(H): # 위아래 삼차원
    for j in range(N): # 세로값
        for k in range(M): # 가로값
            if arr[i][j][k] == 1:
                bfstem.append((i,j,k))
            elif arr[i][j][k] == 0:
                zero_cnt += 1

print(bfs())





# if zero_cnt == 0:
#     print(v[cz][cx][cy])
#
# else:
#     print(-1)
# print(zero_cnt)
# print(v)
# print(bfs())