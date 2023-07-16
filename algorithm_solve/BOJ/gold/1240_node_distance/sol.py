import sys
sys.stdin = open('1240_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(n):
    v = [0] * (N+1)
    v[n] = 1

    q = deque()
    q.append((n, 0))

    while q:
        cn, c_dis = q.popleft()
        if cn == b:
            return c_dis

        for j, dis in arr[cn]:
            if v[j] == 0:
                v[j] = 1
                q.append((j, c_dis + dis))



N, M = map(int,input().split())

arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))


for _ in range(M):
    a, b = map(int,input().split())
    print(bfs(a))