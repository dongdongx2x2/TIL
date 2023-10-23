import sys
sys.stdin = open('1398_input.txt')

input = sys.stdin.readline

T = int(input())
coins = [1, 10, 25]


for _ in range(T):
    n = int(input())
    dp = [10 ** 15 + 1 for _ in range(100)]
    dp[0] = 0
    ans = 0

    for coin in coins:
        for i in range(coin, 100):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    while n:
        ans += dp[n % 100]
        n //= 100
    print(ans)


