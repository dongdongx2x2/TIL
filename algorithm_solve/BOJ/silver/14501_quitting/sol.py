import sys
sys.stdin = open('14501_input.txt')

input = sys.stdin.readline

N = int(input())
T, P = [0], [0]
dp = [0] * (N + 2)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[1])