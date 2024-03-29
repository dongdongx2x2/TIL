import sys
sys.stdin = open('5582_input.txt')

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n1 = len(s1)
n2 = len(s2)

cnt = 0
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            cnt = max(dp[i][j], cnt)
print(cnt)




