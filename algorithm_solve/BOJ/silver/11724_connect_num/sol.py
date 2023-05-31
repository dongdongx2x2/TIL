import sys
sys.stdin = open('11724_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    v[n] = 1
    while q:
        cn = q.popleft()
        for i in arr[cn]:
            if not v[i]:
                v[i] = 1
                q.append(i)

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


v = [0] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not v[i]:
        if not arr[i]:
            cnt += 1
            v[i] = 1
        else:
            bfs(i)
            cnt += 1
print(cnt)