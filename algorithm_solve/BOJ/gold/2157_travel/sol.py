import sys
sys.stdin = open('2157_input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())

flights = [[] for _ in range(n+1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        flights[a].append((b, c))

dp = [[-1] * (n+1) for _ in range(m+1)]
dp[1][1] = 0

for i in range(1, m):
    for j in range(1, n + 1):
        if dp[i][j] == -1:
            continue

        for next_city, score in flights[j]:
            if dp[i+1][next_city] < dp[i][j] + score:
                dp[i+1][next_city] = dp[i][j] + score
mxmx = -1

for i in range(2, m+1):
    if dp[i][n] > mxmx:
        mxmx = dp[i][n]
print(mxmx)
