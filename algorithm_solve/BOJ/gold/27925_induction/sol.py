import sys
sys.stdin = open('27925_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def f(p, x, y, z):
    if p == n:
        return 0
    if dp[p][x][y][z] != -1:
        return dp[p][x][y][z]
    dp[p][x][y][z] = min(
        f(p + 1, a[p + 1], y, z) + min(abs(x - a[p + 1]) % 10, 10 - abs(x - a[p + 1]) % 10),
        f(p + 1, x, a[p + 1], z) + min(abs(y - a[p + 1]) % 10, 10 - abs(y - a[p + 1]) % 10),
        f(p + 1, x, y, a[p + 1]) + min(abs(z - a[p + 1]) % 10, 10 - abs(z - a[p + 1]) % 10)
    )
    return dp[p][x][y][z]

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[[[-1] * 10 for _ in range(10)] for _ in range(10)] for _ in range(n + 1)]

print(f(0, 0, 0, 0))