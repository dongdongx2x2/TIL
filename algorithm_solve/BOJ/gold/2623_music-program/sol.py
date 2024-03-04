import sys
sys.stdin = open('2623_input.txt')

input = sys.stdin.readline
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    if len(result) != n:
        return []
    else:
        return result

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    tem = list(map(int, input().split()))
    num, lst = tem[0], tem[1:]

    for i in range(num-1):
        a, b = lst[i], lst[i+1]
        graph[a].append(b)
        indegree[b] += 1

result = topology_sort()

if not result:
    print(0)
else:
    for i in result:
        print(i)