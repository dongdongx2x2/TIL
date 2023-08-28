import sys
sys.stdin = open('1010_input.txt')

input = sys.stdin.readline

T = int(input())

dp = [[0] * 31 for _ in range(31)]

for i in range(31):
    for j in range(31):
        if i == 1:
            dp[i][j]= j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(T):
    N, M = map(int,input().split())
    print(dp[N][M])
