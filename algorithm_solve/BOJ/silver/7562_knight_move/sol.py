import sys
sys.stdin = open('7562_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(si,sj,arr):

    q = deque()
    q.append((si,sj))
    arr[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            return arr[ei][ej]

        for di, dj in ((1,2),(2,1),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj] + 1

T = int(input())
for _ in range(T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    print(bfs(si,sj,arr)-1)