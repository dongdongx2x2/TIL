import sys
sys.stdin = open('2573_input.txt')

input = sys.stdin.readline
from copy import deepcopy
from collections import deque


def bfs(si, sj, v):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di,cj + dj
            if v[ni][nj] == 0 and arr[ni][nj] >0:
                q.append((ni,nj))
                v[ni][nj] = 1


def solve():
    global arr

    for year in range(1,900000):
        arr_tem = deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:

                    cnt = 0
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                            cnt += 1
                    arr_tem[i][j] -= cnt
                    if arr_tem[i][j] < 0:
                        arr_tem[i][j] = 0
        arr = arr_tem

        cnt = 0
        v = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if v[i][j] == 0 and arr[i][j] > 0:
                    bfs(i, j, v)
                    cnt += 1
                    if cnt > 1:
                        return year
        if cnt == 0:
            return 0



n, m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

print(solve())



