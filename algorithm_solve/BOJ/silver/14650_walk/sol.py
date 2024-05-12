import sys
sys.stdin = open('14650_input.txt')

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
MOD = 1000000009
if n >= 2:
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * 3) % MOD

print(dp[n])