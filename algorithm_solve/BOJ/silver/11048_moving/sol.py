import sys
sys.stdin = open('11048_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] += max(arr[i-1][j], arr[i][j-1])
print(arr[N][M])
