import sys
sys.stdin = open('2302_input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * 41

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
prev = 0

for v in vip:
    ans *= dp[v - prev - 1]
    prev = v
ans *= dp[n-prev]

print(ans)

