import sys
sys.stdin = open('1446_input.txt')

input = sys.stdin.readline

N, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [i for i in range(D+1)]

for i in range(D+1):
    dp[i] = min(dp[i], dp[i-1] + 1)

    for a, b, c in arr:
        if i==a and b<=D and dp[i] + c < dp[b]:
            dp[b] = dp[i] + c
print(dp[D])
