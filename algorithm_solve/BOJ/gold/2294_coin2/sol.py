import sys
sys.stdin = open('2294_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

INF = int(1e9)

coins = set()
for _ in range(n):
    coins.add(int(input()))

dp = [INF] * (k+1)
dp[0] = 0
for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j-coin]+1)

print(-1 if dp[k]==INF else dp[k])