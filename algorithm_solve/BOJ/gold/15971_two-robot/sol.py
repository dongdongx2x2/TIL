import sys
sys.stdin = open('15971_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(graph, start):
    q = deque()
    q.append((start, 0, 0))  # (노드, 총 거리, 최대 통로 길이)

    v = [(-1, -1)] * (n+1)  # (총 거리, 최대 통로 길이)
    v[start] = (0, 0)

    while q:
        cur, dist, max_edge = q.popleft()
        for next_node, weight in graph[cur]:
            if v[next_node][0] == -1:
                new_max_edge = max(max_edge, weight)
                v[next_node] = (dist + weight, new_max_edge)
                q.append((next_node, dist + weight, new_max_edge))

    return v

n, s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist_s = bfs(graph, s)
dist_e = bfs(graph, e)

mimi = int(1e9)

for i in range(1, n+1):
    if dist_s[i][0] != -1 and dist_e[i][0] != -1:
        total = dist_s[i][0] + dist_e[i][0]
        max_edge = max(dist_s[i][1], dist_e[i][1])
        mimi = min(mimi, total - max_edge)

print(mimi)