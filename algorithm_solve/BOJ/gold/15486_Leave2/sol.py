import sys
sys.stdin = open('15486_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])
    if (i+T-1) <= N:
        dp[i+T-1] = max(dp[i-1]+P, dp[i+T-1])
print(dp[N])