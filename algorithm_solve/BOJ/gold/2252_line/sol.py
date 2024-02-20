import sys
sys.stdin = open('2252_input.txt')

input = sys.stdin.readline

def dfs(start):
    v[start] = 1
    for i in graph[start]:
        if not v[i]:
            dfs(i)
    result.append(start)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = []
for i in range(1, n+1):
    if not v[i]:
        dfs(i)

for i in result[::-1]:
    print(i, end=" ")