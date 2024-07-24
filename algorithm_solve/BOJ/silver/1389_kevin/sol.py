import sys
sys.stdin = open('1389_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(start):
    v = [0] * (n + 1)
    v[start] = 1
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        for next_node in graph[cur]:
            if v[next_node] == 0:
                v[next_node] = v[cur] + 1
                q.append(next_node)
    return sum(v)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1, n + 1):
    result.append(bfs(i))

print(result.index(min(result))+1)