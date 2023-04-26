import sys
sys.stdin = open('2565_input.txt')

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a,b))
lst.sort()

dp = [1]*N

for i in range(1, N):
    for j in range(i):

        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N-max(dp))