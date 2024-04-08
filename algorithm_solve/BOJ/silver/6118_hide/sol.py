import sys
sys.stdin = open('6118_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    v[start] = 0

    while q:
        now = q.popleft()

        for next in graph[now]:
            if v[next] == -1:
                v[next] = v[now] + 1
                q.append(next)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [-1] * (n+1)
bfs(1)
mx = max(v)
print(v.index(mx), mx, v.count(mx))