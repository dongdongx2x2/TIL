import sys
sys.stdin = open('2624_input.txt')

input = sys.stdin.readline

t = int(input())
k = int(input())

coins = [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (t + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    p, n = coins[i-1]

    for j in range(t + 1):
        dp[i][j] = dp[i-1][j]

        for x in range(1, n + 1):
            if j >= p * x:
                dp[i][j] += dp[i-1][j-p*x]

            else:
                break
print(dp[k][t])

