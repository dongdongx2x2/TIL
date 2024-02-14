import sys
sys.stdin = open('21278_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = [1,2,1e9]

for b1 in range(1, n+1):
    for b2 in range(b1+1, n+1):
        time = 0

        for i in range(1, n+1):
            time += min(graph[i][b1], graph[i][b2]) * 2

        if time < ans[-1]:
            ans = [b1, b2, time]
print(*ans)