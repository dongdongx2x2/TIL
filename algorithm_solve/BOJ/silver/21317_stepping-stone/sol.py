import sys

sys.stdin = open('21317_input.txt')

input = sys.stdin.readline

N = int(input())

lst = [[0, 0]]

for _ in range(N-1):
    small, big = map(int, input().split())
    lst.append([small, big])

K = int(input())

if N == 1:
    print(0)
    exit()
elif N == 2:
    print(lst[1][0])
    exit()

dp = [[5001, 5001] for _ in range(N+1)]

dp[1][0] = 0
dp[2][0] = lst[1][0]
dp[3][0] = min(lst[1][0] + lst[2][0], lst[1][1])

for i in range(4, N+1):
    dp[i][0] = min(lst[i-1][0] + dp[i-1][0], lst[i-2][1] + dp[i-2][0])
    dp[i][1] = min(min(lst[i-1][0] + dp[i-1][1], lst[i-2][1] + dp[i-2][1]), K + dp[i-3][0])

# print(dp)
print(min(dp[N][0], dp[N][1]))