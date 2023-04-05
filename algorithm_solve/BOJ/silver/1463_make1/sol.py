import sys
sys.stdin = open('1463_input.txt')

input = sys.stdin.readline

N = int(input())

dp = [0]* (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
# print(dp)
print(dp[N])
# for i in range(2, N+1):
#
#     if i % 2 == 0 and i % 3 == 0:
#         dp[i] = min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1)
#
#     elif i % 2 == 0:
#         dp[i] = min(dp[i-1]+1,dp[i//2]+1)
#
#     elif i % 3 == 0:
#         dp[i] = min(dp[i-1]+1, dp[i//3]+1)
#
#     else:
#         dp[i] = dp[i-1] + 1
#
# print(dp[N])


