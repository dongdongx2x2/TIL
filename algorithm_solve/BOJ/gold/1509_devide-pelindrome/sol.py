import sys
sys.stdin = open('1509_input.txt')

input = sys.stdin.readline

string = input().rstrip()

n = len(string)

is_palindrome = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    is_palindrome[i][i] = True
for i in range(1, n):
    if string[i - 1] == string[i]:
        is_palindrome[i][i + 1] = True

for length in range(2, n):
    for start in range(1, n - length + 1):
        end = start + length
        if string[start - 1] == string[end - 1] and is_palindrome[start + 1][end - 1]:
            is_palindrome[start][end] = True

dp = [0] + [n] * n

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if is_palindrome[j][i]:
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[n])