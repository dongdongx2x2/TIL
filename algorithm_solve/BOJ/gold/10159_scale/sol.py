import sys
sys.stdin = open('10159_input.txt')

input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

arr = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr[i][i] = 0


for _ in range(M):
    a, b = map(int,input().split())
    arr[a][b] = 1


for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if arr[i][j] == INF and arr[j][i] == INF:
            cnt += 1
    print(cnt)
