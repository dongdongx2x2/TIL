import sys
sys.stdin = open('2458_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0

for i in range(1, n + 1):
    known = True
    for j in range(1, n + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            known = False
            break
    if known:
        cnt += 1
print(cnt)
