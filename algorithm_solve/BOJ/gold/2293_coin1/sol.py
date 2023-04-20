import sys
sys.stdin = open('2293_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1

coins = []
for _ in range(n):
    coins.append(int(input()))


for coin in coins:
    for j in range(1, k+1):
        if j-coin >= 0:
            dp[j] += dp[j-coin]

print(dp[k])
