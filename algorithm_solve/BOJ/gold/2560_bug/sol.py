import sys
sys.stdin = open('2560_input.txt')

input = sys.stdin.readline

a, b, d, N = map(int, input().split())

dp = [0] * (N+1)
dp[0] = 1

prefix = 0

for i in range(1, N + 1):
    prefix = (prefix + dp[i-a] - dp[i-b] + 1000) % 1000
    dp[i] = prefix


ans = 0
for i in range(max(0,N-d+1), N+1):
    ans = (ans + dp[i]) % 1000


print(ans)