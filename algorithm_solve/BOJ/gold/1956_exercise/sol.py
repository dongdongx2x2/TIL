import sys
sys.stdin = open('1956_input.txt')

input = sys.stdin.readline

V, E = map(int, input().split())

INF = float("INF")
arr = [[INF] * (V+1) for _ in range(V+1)]

# for i in range(V+1):
#     arr[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

mxmx = INF
for i in range(V+1):
    mxmx = min(mxmx, arr[i][i])

print(mxmx if mxmx != INF else -1)