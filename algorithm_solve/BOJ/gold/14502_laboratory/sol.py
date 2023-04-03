import sys
sys.stdin = open('14502_input.txt')
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

def bfs():
    global mxmx

    zero_cnt = len(zero_lst)-3

    q = deque()
    for si,sj in bfstem:
        q.append((si,sj))

    while q:
        ci, cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni< N and 0<= nj < M and tem_arr[ni][nj] == 0:
                tem_arr[ni][nj] = 2
                q.append((ni,nj))
                zero_cnt -= 1
    mxmx = max(zero_cnt, mxmx)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


zero_lst = []

bfstem = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_lst.append((i,j))
        elif arr[i][j] == 2:
            bfstem.append((i,j))
mxmx = 0
for zero in combinations(zero_lst, 3):

    tem_arr = copy.deepcopy(arr)

    for x, y in zero:
        tem_arr[x][y] = 1

    # print(tem_arr)
    bfs()

print(mxmx)