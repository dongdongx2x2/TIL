import sys
sys.stdin = open('9507_input.txt')

input = sys.stdin.readline


def koong(n):
    dp = [1, 1, 2, 4] + [0] * 64

    if n <= 3:
        return dp[n]

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    return dp[n]


t = int(input())

for _ in range(t):
    n = int(input())
    print(koong(n))