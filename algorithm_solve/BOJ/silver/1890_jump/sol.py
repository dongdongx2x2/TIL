import sys
sys.stdin = open('1890_input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and arr[i][j]>0:

            if j+arr[i][j] < N:
                dp[i][j+arr[i][j]] += dp[i][j]

            if i+arr[i][j] < N:
                dp[i+arr[i][j]][j] += dp[i][j]

print(dp[N-1][N-1])


