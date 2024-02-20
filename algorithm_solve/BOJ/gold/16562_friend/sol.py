import sys
sys.stdin = open('16562_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    v[start] = 1

    min_money = lst[start]
    while q:
        now = q.popleft()

        for next in graph[now]:
            if not v[next]:
                min_money = min(min_money, lst[next])
                q.append(next)
                v[next] = 1

    return min_money

n, m, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))
v = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

money = 0
for i in range(1, n+1):
    if not v[i]:
        money += bfs(i)

if money <= k:
    print(money)
else:
    print("Oh no")