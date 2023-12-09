import sys

sys.stdin = open('13301_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * 81
dp[0] = 4
dp[1] = 6

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N - 1])
