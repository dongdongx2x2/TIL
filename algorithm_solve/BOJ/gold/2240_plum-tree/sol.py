import sys
sys.stdin = open('2240_input.txt')

input = sys.stdin.readline

t, w = map(int, input().split())

lst = [0] + [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):

    if lst[i] == 1:
        dp[i][0] = dp[i-1][0] + 1

    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w + 1):

        if (lst[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        elif (lst[i] == 1 and j % 2 == 0):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))
