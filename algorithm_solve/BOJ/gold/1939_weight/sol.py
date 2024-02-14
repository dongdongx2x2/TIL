import sys
sys.stdin = open('1939_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(c):
    q = deque([one])
    v = [False] * (n + 1)
    v[one] = True

    while q:
        x = q.popleft()
        for y, weight in graph[x]:
            if not v[y] and weight >= c:
                v[y] = True
                q.append(y)
    return v[two]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

one, two = list(map(int, input().split()))

s, e = 1, 1000000000
ans = 0

while s <= e:
    mid = (s + e) // 2
    if bfs(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
