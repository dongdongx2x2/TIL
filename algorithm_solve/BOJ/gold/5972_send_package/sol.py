import sys
sys.stdin = open('5972_input.txt')

input = sys.stdin.readline

from heapq import heappop,heappush

INF = int(1e9)

N, M = map(int,input().split())

graph = [[] for i in range(N+1)]
dis = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijk(start):
    q = []
    heappush(q, (0,start))
    dis[start] = 0

    while q:
        cost, now = heappop(q)
        if dis[now] < cost:
            continue
        for i in graph[now]:
            rep = cost + i[1]

            if rep < dis[i[0]]:
                dis[i[0]] = rep
                heappush(q,(rep,i[0]))

dijk(1)
print(dis[N])