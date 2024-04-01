import sys
sys.stdin = open('10282_input.txt')

input = sys.stdin.readline
import heapq

def dijk(start, graph, n):
    INF = 1e9

    dis = [INF] * (n+1)
    dis[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        c_dis, c_node = heapq.heappop(hq)

        if dis[c_node] < c_dis:
            continue

        for adj, w in graph[c_node]:
            cost = c_dis + w
            if cost < dis[adj]:
                dis[adj] = cost
                heapq.heappush(hq, (cost, adj))

    tem = []
    for d in dis:
        if d != INF:
            tem.append(d)
    return len(tem), max(tem)

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))

    cnt, time = dijk(c, graph, n)
    print(cnt, time)