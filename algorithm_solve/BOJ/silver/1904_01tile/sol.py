import sys
sys.stdin = open('1904_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2
for i in range(3, N+2):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[N])