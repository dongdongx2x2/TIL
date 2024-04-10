import sys
sys.stdin = open('2602_input.txt')

input = sys.stdin.readline

goal = input().rstrip()
angel = input().rstrip()
devil = input().rstrip()

n = len(goal)
m = len(angel)

dp = [[[0] * 2 for _ in range(m+1)] for _ in range(n+1)]


for i in range(m):
    if angel[i] == goal[0]:
        dp[1][i][1] = 1
    if devil[i] == goal[0]:
        dp[1][i][0] = 1

for i in range(1, n):
    for j in range(m):
        if goal[i] == angel[j]:
            for k in range(j):
                dp[i+1][j][1] += dp[i][k][0]

        if goal[i] == devil[j]:
            for k in range(j):
                dp[i+1][j][0] += dp[i][k][1]

ans = 0

for i in range(m):
    ans += dp[n][i][0] + dp[n][i][1]
print(ans)