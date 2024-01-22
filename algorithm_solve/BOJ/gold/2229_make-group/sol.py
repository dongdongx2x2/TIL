import sys
sys.stdin = open('2229_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i-1]
    mi = lst[i-1]
    mx = lst[i-1]

    for j in range(i, 0, -1):
        mi = min(mi, lst[j-1])
        mx = max(mx, lst[j-1])
        dp[i] = max(dp[i], dp[j-1] + mx - mi)

print(dp[-1])