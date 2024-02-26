import sys
sys.stdin = open('16947_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10000)
from collections import deque

def dfs(d, cnt):
    global is_cycle

    for i in graph[d[-1]]:
        if i == d[0] and cnt >= 2:
            for j in d:
                dis[j] = 0
            is_cycle = True
            return
        if not v[i]:
            v[i] = 1
            dfs(d + [i], cnt + 1)
            v[i] = 0

def bfs():
    q = deque()
    for i in range(1, n+1):
        if dis[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for next in graph[now]:
            if dis[next] == -1:
                q.append(next)
                dis[next] = dis[now] + 1


n = int(input())
graph = [[] for _ in range(n+1)]
dis = [-1] * (n+1)
v = [0] * (n+1)
is_cycle = False

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if is_cycle:
        break
    v[i] = 1
    dfs([i], 0)
    v[i] = 0
bfs()
print(*dis[1:])



