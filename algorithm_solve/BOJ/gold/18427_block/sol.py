import sys
sys.stdin = open('18427_input.txt')

input = sys.stdin.readline

n, m, h = map(int, input().split())

blocks = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (h + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, h + 1):
        dp[i][j] = dp[i-1][j]

        for block in blocks[i-1]:
            if j >= block:
                dp[i][j] += dp[i-1][j-block]

    for j in range(1, h + 1):
        dp[i][j] %= 10007
print(dp[n][h])