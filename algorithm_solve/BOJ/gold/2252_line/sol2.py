import sys
sys.stdin = open('2252_input.txt')

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
ans = []
while q:
    tem = q.popleft()
    ans.append(tem)
    for i in graph[tem]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)
print(*ans)


