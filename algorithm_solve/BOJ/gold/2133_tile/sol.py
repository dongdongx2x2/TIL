import sys
sys.stdin = open('2133_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0] * 31
dp[0] = 1
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2):
        dp[i] += dp[j]*2

# print(dp)
print(dp[N])
