import sys
sys.stdin = open('1719_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]
arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    arr[a][b] = b
    arr[b][a] = a

# print(graph)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                arr[a][b] = arr[a][k]
                # arr[a][b] = b
            # graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            arr[i][j] = '-'
        print(arr[i][j], end=' ')
    print()
