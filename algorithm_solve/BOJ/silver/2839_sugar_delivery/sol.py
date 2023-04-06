import sys
sys.stdin = open('2839_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [5001]*5001

dp[3] = 1
dp[5] = 1

for i in range(3, N+1):
    dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)


print(dp[N] if dp[N] != 5001 else -1)

