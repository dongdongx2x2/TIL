import sys
sys.stdin = open('7576_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():

    v = [[0] * M for _ in range(N)]
    q = deque()


    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zero_cnt += 1
            elif arr[i][j] == 1:
                q.append((i,j))
                v[i][j] = 1

    while q:
        ci,cj = q.popleft()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))
                zero_cnt -= 1

    if zero_cnt == 0:
        return v[ci][cj]-1

    else:
        return -1


M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs())