import sys
sys.stdin = open('7579_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
on = [0] + list(map(int, input().split()))
off = [0] + list(map(int, input().split()))

dp = [[0] * (sum(off) + 1) for _ in range(n+1)]
ans = sum(off)

for i in range(1, n+1):
    cost = off[i]
    memory = on[i]

    for j in range(sum(off) + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

        if dp[i][j] >= m:
            ans = min(ans, j)
print(ans)