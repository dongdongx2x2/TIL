import sys

sys.stdin = open('5557_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

dp[0][lst[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + lst[i] <= 20:
                dp[i][j+lst[i]] += dp[i-1][j]
            if j - lst[i] >= 0:
                dp[i][j-lst[i]] += dp[i-1][j]
print(dp[N-2][lst[-1]])

