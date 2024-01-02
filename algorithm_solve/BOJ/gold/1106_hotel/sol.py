import sys
sys.stdin = open('1106_input.txt')

input = sys.stdin.readline

c, n = map(int, input().split())

lst = []
for _ in range(n):
    cost, people = map(int, input().split())
    lst.append((cost,people))

dp = [1e9] * (c + 101)
dp[0] = 0

for cost, people in lst:
    for i in range(people, c + 101):
        dp[i] = min(dp[i-people] + cost, dp[i])

print(min(dp[c:]))