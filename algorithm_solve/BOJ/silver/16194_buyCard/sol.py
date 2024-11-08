import sys
sys.stdin = open('16194_input.txt')

input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = P[i]
    for j in range(1, i):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[N])