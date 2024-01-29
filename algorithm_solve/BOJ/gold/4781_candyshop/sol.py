import sys
sys.stdin = open('4781_input.txt')

input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n = int(n)
    if not n and not m:
        break

    m = int(m * 100 + 0.5)
    dp = [0] * (m + 1)

    for _ in range(n):
        c, p = map(float, input().split())
        c = int(c)
        p = int(p * 100 + 0.5)

        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i-p] + c)

    print(dp[m])


