import sys
sys.stdin = open('18352_input.txt')

input = sys.stdin.readline
from collections import deque


def bfs(n):
    q = deque()
    q.append(n)
    v[n] = 0
    while q:
        cn = q.popleft()

        for j in arr[cn]:
            if v[j] == -1:
                v[j] = v[cn] + 1
                q.append(j)

N, M, K, X = map(int,input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)

# print(arr)
v = [-1] * (N+1)
bfs(X)
# print(v)

if v.count(K) == 0:
    print(-1)
else:
    for i in range(1, N+1):
        if v[i] == K:
            print(i)

