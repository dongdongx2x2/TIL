import sys

sys.stdin = open('13699_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[N])
