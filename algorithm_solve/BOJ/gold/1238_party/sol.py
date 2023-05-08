import sys
sys.stdin = open('1238_input.txt')

input = sys.stdin.readline
from heapq import heappop, heappush

N, M, X = map(int,input().split())

INF = int(1e9)
arr = [[] for _ in range(N+1)]
vis = [INF] * (N+1)


for _ in range(M):
    a, b, c = map(int,input().split())
    arr[a].append((b,c))

def dijk(start):
    q = []
    heappush(q,(0,start))
    vis[start] = 0

    while q:
        dist, now = heappop(q)

        if vis[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < vis[i[0]]:
                vis[i[0]] = cost
                heappush(q, (cost, i[0]))

v = [0] * (N+1)
dijk(X)
# print(vis)
for i in range(1, N+1):
    v[i] = vis[i]
# print(v)


for i in range(1, N+1):
    vis = [INF] * (N + 1)
    dijk(i)
    v[i] += vis[X]
print(max(v))

