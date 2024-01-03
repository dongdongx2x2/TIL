import sys
sys.stdin = open('1958_input.txt')

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
str3 = input().rstrip()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)


dp = [[[0] * (len1 + 1) for _ in range(len2 + 1)] for _ in range(len3 + 1)]

for i in range(1, len3 + 1):
    for j in range(1, len2 + 1):
        for k in range(1, len1 + 1):
            if str3[i-1] == str2[j-1] == str1[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])