import sys
sys.stdin = open('11726_input.txt')

input = sys.stdin.readline

def tile_ways(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]

n = int(input())

print(tile_ways(n))