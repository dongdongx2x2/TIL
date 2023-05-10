import sys
sys.stdin = open('2156_input.txt')

input = sys.stdin.readline

n = int(input())

lst = [0] * 10001
for i in range(n):
    lst[i+1] = (int(input()))

dp = [0] * 10001
#
# print(lst)
# print(dp)

dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
# print(dp)

for i in range(3, n+1):
    dp[i] = max(lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3], dp[i-1])

print(dp[n])