import sys
sys.stdin = open('11780_input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]
arr = [[()] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)
    arr[a][b] = (a,b)
# print(arr)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                arr[a][b] = arr[a][k] + arr[k][b][1:]

            # graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(arr[i][j]), *arr[i][j])

