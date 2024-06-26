import sys
sys.stdin = open('14925_input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]

max_len = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            if i == 0 or j == 0:
                dp[i][j] = 1

            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            max_len = max(max_len, dp[i][j])
print(max_len)
