import sys
sys.stdin = open('1325_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    v = [0] * (n + 1)
    v[start] = 1

    cnt = 0

    while q:
        now = q.popleft()

        for next in graph[now]:
            if not v[next]:
                v[next] = 1
                q.append(next)
                cnt += 1
    return cnt


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []
for i in range(1, n + 1):
    ans.append(bfs(i))

mx = max(ans)

for i in range(n):
    if mx == ans[i]:
        print(i + 1, end=" ")