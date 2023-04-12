import sys
sys.stdin = open('1504_input.txt')

input = sys.stdin.readline

from heapq import heappop, heappush
INF = int(1e9)

N, E = map(int,input().split())

graph = [[] for i in range(N+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
# print(graph)
v1, v2 = map(int,input().split())


def dijk(start):
    v = [INF] * (N + 1)
    q = []
    heappush(q,(0,start))
    v[start] = 0
    while q:
        dis, now = heappop(q)

        if v[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]
            if cost < v[i[0]]:
                v[i[0]] = cost
                heappush(q,(cost,i[0]))

    return v

tem1 = dijk(1)
tem2 = dijk(v1)
tem3 = dijk(v2)


ans = min(tem1[v1] + tem2[v2] + tem3[N], tem1[v2] + tem3[v1] + tem2[N])

print(ans if ans < INF else -1)

