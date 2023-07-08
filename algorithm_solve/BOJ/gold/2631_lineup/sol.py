import sys
sys.stdin = open('2631_input.txt')

input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]

dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(N - max(dp))



