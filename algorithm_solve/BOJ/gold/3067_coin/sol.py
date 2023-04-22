import sys
sys.stdin = open('3067_input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    coins = list(map(int,input().split()))

    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for j in range(1, M+1):
            if j-coin >= 0:
                dp[j] += dp[j-coin]

    print(dp[M])