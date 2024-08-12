import sys
sys.stdin = open('1082_input.txt')

input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))
m = int(input())

dp = [-int(1e9) for _ in range(m+1)]

for i in range(n-1, -1, -1):
    x = cost[i]
    for j in range(x, m + 1):
        dp[j] = max(dp[j], dp[j-x]*10 + i, i)

print(dp[m])