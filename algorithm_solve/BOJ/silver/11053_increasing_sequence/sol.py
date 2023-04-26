import sys
sys.stdin = open('11053_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))