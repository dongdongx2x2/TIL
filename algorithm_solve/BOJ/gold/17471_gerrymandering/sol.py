import sys
sys.stdin = open('17471_input.txt')

input = sys.stdin.readline

from itertools import combinations
from collections import deque

def bfs(arr):
    s = arr[0]
    q = deque()
    q.append(s)

    v = set()
    v.add(s)

    sm = 0

    while q:
        now = q.popleft()
        sm += lst[now]

        for i in graph[now]:
            if i in arr and i not in v:
                q.append(i)
                v.add(i)
    return sm, len(v)

n = int(input())
lst = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]


for i in range(n):
    tem = list(map(int, input().split()))[1:]
    for j in tem:
        graph[i+1].append(j)

ans = 1e9

for i in range(1, n//2 + 1):
    combis = list(combinations(range(1,n+1), i))

    for combi in combis:
        sm1, node1 = bfs(combi)
        sm2, node2 = bfs([i for i in range(1, n+1) if i not in combi])

        if node1 + node2 == n:
            ans = min(ans, abs(sm1-sm2))

print(ans if ans != 1e9 else -1)