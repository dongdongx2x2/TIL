import sys
sys.stdin = open('11066_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]
    sm = [0] * (k + 1)


    for i in range(1, k + 1):
        sm[i] = sm[i - 1] + files[i - 1]


    for l in range(2, k + 1):
        for i in range(k - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')


            for m in range(i, j):
                cost = dp[i][m] + dp[m + 1][j] + sm[j + 1] - sm[i]
                dp[i][j] = min(dp[i][j], cost)
    print(dp[0][k - 1])