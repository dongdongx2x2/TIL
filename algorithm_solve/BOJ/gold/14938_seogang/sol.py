import sys
sys.stdin = open('14938_input.txt')

input = sys.stdin.readline

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0


for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# print(graph)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0

for i in range(1, n+1):
    mxmx = 0

    for j in range(1, n+1):
        if graph[i][j] <= m:
            mxmx += items[j]
    ans = max(mxmx, ans)
print(ans)


