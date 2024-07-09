import sys
sys.stdin = open('17845_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, k + 1):
    importance, time = map(int, input().split())

    for j in range(1, n + 1):
        if j < time:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + importance)

print(dp[k][n])
