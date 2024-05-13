import sys
sys.stdin = open('2591_input.txt')

input = sys.stdin.readline

s = input().rstrip()

dp = [0] * (len(s) + 1)
dp[0] = 1

for i in range(1, len(s) + 1):
    if 1 <= int(s[i-1:i]) <= 9:
        dp[i] += dp[i-1]

    if i > 1 and 10 <= int(s[i-2:i]) <= 34:
        dp[i] += dp[i-2]
print(dp[len(s)])